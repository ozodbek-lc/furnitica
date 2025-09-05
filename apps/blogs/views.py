from datetime import timedelta

from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone

from apps.blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


def blogs_list_view(request):
    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()
    blogs = BlogModel.objects.filter(
        status=BlogModel.BlogStatus.PUBLISHED
    )
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
        blog = BlogModel.objects.get(id=pk)
    except BlogModel.DoesNotExist:
        return render(request,'404.html')

    categories = BlogCategoryModel.objects.all()
    tags = BlogTagModel.objects.all()

    context = {
        "blog":blog,
    }
    return render(
        request,'blog-detail.html',
        context
    )


