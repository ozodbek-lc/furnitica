from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.products_grid_view,name='grid'),
    path('product-detail/',views.products_detail_view,name='detail'),
    path('product-checkout/',views.products_checkout_view,name='checkout'),
    path('product-cart/',views.products_cart_view,name='cart'),
]