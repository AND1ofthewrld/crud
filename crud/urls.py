"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from roles.views import index, article_page, article_create, article_delete, article_edit
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('myapp/', include('roles.urls')),
    path('article_page/', article_page, name='article_page'),
    path('article_create/', article_create, name='article_create'),
    path('article_delete/', article_delete, name='article_delete'),
     path('article/edit/<int:article_id>/', article_edit, name='article_edit'),
]