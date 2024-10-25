from django.shortcuts import render,redirect
from .models import Product, RelatedImages
from payment.models import Payment
from django.conf import settings
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
    print(paystack_public_key)

    context ={
        'payment':payment,
        'paystack_public_key':paystack_public_key,
    }
    return render(request,'html/makePaymentNew.html',context)

def checkout(request):
    if request.method == 'POST':
        if 'pay' in request.POST:
            firstName = request.POST.get('fname')
            lastName = request.POST.get('lname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            orderNotes = request.POST.get('orderNotes')
            deliveryAddress = request.POST.get('deliveryAddress')
            deliveryInfo = request.POST.get('deliveryInfo')
            cart_total = request.POST.get('cart-total')

            print(firstName,lastName,email,phone,orderNotes,deliveryAddress,deliveryInfo,cart_total)
            payment = Payment(first_name=firstName,last_name=lastName,email=email,phone=phone,order_notes=orderNotes,delivery_address=deliveryAddress,additional_info=deliveryInfo,amount=float(cart_total))
            payment.save()
            print(payment)


            return redirect(makePayment,payment.ref)

     
    return render(request,'html/checkout.html')

