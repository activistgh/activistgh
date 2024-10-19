from django.urls import path
from .views import shop, productDetail, checkout

urlpatterns =[
    path('shop/',shop,name='shop'),
    path('productDetail/<str:unique_id>/',productDetail,name='productDetail'),
    path('checkout',checkout,name='checkout'),
]