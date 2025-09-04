from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('',views.blogs_list_view,name='list'),
    path('blogs-detail/',views.blogs_detail_view,name='detail'),
]