from django.shortcuts import render
from apps.blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


def blogs_list_view(request):
    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()
    blogs = BlogModel.objects.filter(
        status=BlogModel.BlogStatus.PUBLISHED
    )

    cat_id = request.GET.get('cat')
    if cat_id:
        blogs = blogs.filter(category_id=cat_id)
    tag_id = request.GET.get('tag')
    if cat_id:
        blogs = blogs.filter(category_id=tag_id)
    context = {
        "blogs":blogs,
        "categories": categories,
        "tags": tags,
    }
    return render(
        request,'blog-list-sidebar-left.html',
        context
    )


def blogs_detail_view(request,pk):
    try:
        blogs = BlogModel.objects.get(id=pk)
    except BlogModel.DoesNotExist:
        return render(request,'404.html')

    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()


    context = {
        "blog":blogs,
        "categories": categories,
        "tags": tags,
    }
    return render(
        request,'blog-detail.html',
        context
    )


