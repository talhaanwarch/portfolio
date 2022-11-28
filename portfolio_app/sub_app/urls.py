from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.blog_page,name='blog'),
    path('demo/',views.demo_page,name='demo'),
    path('demo/nlp/',views.nlp_demo,name='nlpdemo'),
    path('demo/audio/',views.audio_demo,name='audiodemo'),
    path('demo/image/',views.image_demo,name='imagedemo'),
    path('demo/vitals/',views.vitals_demo,name='vitalsdemo'),
    path('blog/<slug:slug>', views.single_post),
    ]