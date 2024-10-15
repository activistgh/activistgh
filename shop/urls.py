from django.urls import path
from .views import shop, productDetail

urlpatterns =[
    path('shop/',shop,name='shop'),
    path('productDetail/<str:unique_id>/',productDetail,name='productDetail'),
]