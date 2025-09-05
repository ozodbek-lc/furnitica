from django.shortcuts import render, get_object_or_404
from .models import ProductModel, CategoryModel, CatalogModel, ColorModel, TagModel

def product_checkout_view(request):
    return render(request,'product-checkout.html')

def product_cart_view(request):
    return render(request,'product-cart.html')


def product_grid_view(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    catalogs = CatalogModel.objects.all()

    return render(request, 'product-grid-sidebar-left.html', {
        'products': products,
        'categories': categories,
        'catalogs': catalogs,
    })


def product_detail_view(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)

    return render(request, 'product-detail.html', {
        'product': product
    })


def page_404(request, exception):
    return render(request, '404.html', status=404)