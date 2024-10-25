from django.urls import path
from .views import shop, productDetail, checkout, makePayment

urlpatterns =[
    path('shop/',shop,name='shop'),
    path('productDetail/<str:unique_id>/',productDetail,name='productDetail'),
    path('checkout',checkout,name='checkout'),
    path('makePayment/<str:ref>/',makePayment,name='makePayment')
]