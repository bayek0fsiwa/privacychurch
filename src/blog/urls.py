from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogHome, name='homeHome'),
    # path('blog/', views.blogPost, name='homePost'),
    path('blog/<slug>', views.blogPost, name='homePost'),
]
