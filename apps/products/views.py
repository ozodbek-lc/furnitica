from django.shortcuts import render
from .models import ProductModel, CategoryModel, CatalogModel, TagModel, ColorModel



def product_checkout_view(request):
    return render(request,'product-checkout.html')

def product_cart_view(request):
    return render(request,'product-cart.html')


def product_grid_view(request):
    product = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    catalogs = CatalogModel.objects.all()
    tags = TagModel.objects.all()
    colors = ColorModel.objects.all()

    return render(request, 'product-grid-sidebar-left.html', {
        'products': product,
        'categories': categories,
        'catalogs': catalogs,
        'tags': tags,
        'color': colors,
    })


def product_detail_view(request,pk):
    try:
        product = ProductModel.objects.get(id=pk)
    except ProductModel.DoesNotExist:
        return render(request, '404.html')

    categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()

    context = {
        "products": product,
        "categories": categories,
        "tags": tags,
    }
    return render(
        request, 'product-detail.html',
        context
    )