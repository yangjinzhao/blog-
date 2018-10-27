"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from .views import *
app_name='articles'
urlpatterns = [
   path('detail/<int:articleid>/' ,article_detail,name='article_detail'),
   path('add_comment/<int:articleid>/',add_comment,name='add_comment'),
   path('add_love/',add_love,name='add_love'),
   path('add_article',add_article,name='add_article')
]
