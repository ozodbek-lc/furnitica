from django.shortcuts import render
from .models import ProductModel, CategoryModel, CatalogModel, TagModel, ColorModel



def product_checkout_view(request):
    return render(request,'product-checkout.html')

def product_cart_view(request):
    return render(request,'product-cart.html')


def product_grid_view(request):
    products = ProductModel.objects.all()
    categories = CategoryModel.objects.all()
    catalogs = CatalogModel.objects.all()
    tags = TagModel.objects.all()
    colors = ColorModel.objects.all()


    cat_id = request.GET.get('cat')
    if cat_id:
        products = products.filter(category_id=cat_id)
    context = {
        'products': products,
        'categories': categories,
        'catalogs': catalogs,
        'tags': tags,
        'colors': colors,
    }

    return render(request,
                  'product-grid-sidebar-left.html',
                  context
                  )


def product_detail_view(request,pk):
    try:
        products = ProductModel.objects.get(id=pk)
    except ProductModel.DoesNotExist:
        return render(request, '404.html')

    categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()
    colors = ColorModel.objects.all()

    context = {
        "product": products,
        "categories": categories,
        "tags": tags,
        'colors': colors,
    }
    return render(
        request, 'product-detail.html',
        context
    )