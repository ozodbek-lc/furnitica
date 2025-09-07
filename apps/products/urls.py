from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.product_grid_view,name='grid'),
    path('<int:pk>/',views.product_detail_view,name='detail'),
    path('product-checkout/',views.product_checkout_view,name='checkout'),
    path('product-cart/',views.product_cart_view,name='cart'),
]