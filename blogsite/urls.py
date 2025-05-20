"""
URL configuration for blogsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from blogs.api import blogRouter
from blogs import views  # frontend views

api = NinjaAPI()
api.add_router("/blogs/", blogRouter)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', views.blog_list, name='blog_list'),           # list all blogs
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # single blog
]
