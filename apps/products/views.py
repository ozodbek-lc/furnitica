from django.shortcuts import render

def products_grid_view(request):
    return render(request,'product-grid-sidebar-left.html')

def products_detail_view(request):
    return render(request,'product-detail.html')

def products_checkout_view(request):
    return render(request,'product-checkout.html')

def products_cart_view(request):
    return render(request,'product-cart.html')
