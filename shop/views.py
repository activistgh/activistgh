from django.shortcuts import render,redirect
from .models import Product, RelatedImages
from .forms import DeliveryStatusUpdateForm
from payment.models import Payment
from django.conf import settings 
from .models import Cart, CartObject
import ast
import json
# Create your views here.

def shop(request):
    products = Product.objects.all().order_by('id')
    context ={
        'products':products,
    }
    return render(request,'html/shop.html',context)

def productDetail(request,unique_id):
    product = Product.objects.get(unique_id=unique_id)
    related = Product.objects.all().exclude(name = product.name).filter(tag=product.tag)[:3]
    relatedImages = RelatedImages.objects.all().filter(product=product)
    context ={
        'product':product,
        'related':related,
        'relatedImages':relatedImages,
    }
    return render(request,'html/productDetail.html',context)


def makePayment(request,ref):
    payment = Payment.objects.get(ref=ref)
    paystack_public_key = settings.PAYSTACK_PUBLIC_KEY
    

    context ={
        'payment':payment,
        'paystack_public_key':paystack_public_key,
    }
    return render(request,'html/makePaymentNew.html',context)

def checkout(request):
    if request.method == 'POST':
        if 'pay' in request.POST:
            cartData = request.POST.get('cartData')
            cartData =ast.literal_eval(cartData)

            

            # delivery info 
            firstName = request.POST.get('fname')
            lastName = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            orderNotes = request.POST.get('orderNotes')
            deliveryAddress = request.POST.get('deliveryAddress')
            deliveryInfo = request.POST.get('deliveryInfo')
            cart_total = request.POST.get('cart-total')

            payment = Payment(first_name=firstName,last_name=lastName,email=email,phone=phone,order_notes=orderNotes,delivery_address=deliveryAddress,additional_info=deliveryInfo,amount=float(cart_total))
            payment.save()
            
            # on payment save create cart for payment
            cart = Cart.objects.get_or_create(payment=payment) # create cart for payment
            cart[0].save()

            # loop through cart object list to append to cart
            for obj in cartData:
                product = Product.objects.get(unique_id=obj['product_id'])
                cartObj = CartObject(cart=cart[0],product=product,size=obj['selectedSize'],quantity=obj['quantity'] )
                cartObj.save()


            return redirect(makePayment,payment.ref)

     
    return render(request,'html/checkout.html')


def orderSuccess(request,ref):
    payment = Payment.objects.get(ref=ref)
    payment.verified = True
    payment.save()

    # cart 
    cart = Cart.objects.get(payment=payment)

    context ={
        'payment':payment,
        'cart':cart,
    }
    return render(request,'html/orderSuccess.html',context)

def orderDetails(request,ref):
    payment = Payment.objects.get(ref=ref)
    DeliveryStatusUpdateFormCreator = DeliveryStatusUpdateForm(instance=payment)

    if request.method == 'POST':
        if 'updateDeliveryStatus' in request.POST:
            DeliveryStatusUpdateFormCreator = DeliveryStatusUpdateForm(request.POST, instance=payment)
            if DeliveryStatusUpdateFormCreator.is_valid():
                DeliveryStatusUpdateFormCreator.save()
                return redirect(f'/orders/list/')
            else:
                print('Form errors:', DeliveryStatusUpdateFormCreator.errors) 
            

    context = {
        'payment':payment,
        'DeliveryStatusUpdateFormCreator':DeliveryStatusUpdateFormCreator,

    }
    print(payment)
    return render(request,'html/orderDetails.html',context)