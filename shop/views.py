from django.shortcuts import render
from .models import Product, RelatedImages
# Create your views here.

def shop(request):
    products = Product.objects.all()
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

def checkout(request):
    return render(request,'html/checkout.html')