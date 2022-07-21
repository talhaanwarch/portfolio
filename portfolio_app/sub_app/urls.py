from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.blog_page,name='blog'),
    path('demo/',views.demo_page,name='demo'),
    path('blog/<slug:slug>', views.single_post),
    ]