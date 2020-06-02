"""Bolg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import IndexView
from django.urls import path,re_path,include
from .views import (IndexView, DetailView, MessageView, AboutView, DonateView, ExchangeView, ProjectView, QuestionView, LinkView)
urlpatterns = [
    path('',IndexView.as_view(template_name='index.html'),name='index'),
    path('admin/', admin.site.urls),
    
    # 其他页面需要显示的路由
    re_path(r'^category/(?P<bigslug>.*?)/(?P<slug>.*?)', IndexView.as_view(template_name='content.html'), name='category'),
    
    #自己介绍的路由
    path('category/about/', AboutView, name='about'),
    
    #其他页面的路由
    # 给我留言
    path('category/message/', MessageView, name='message'),
    # 关于自己
    path('category/about/', AboutView, name='about'),
    # 赞助作者
    path('category/donate/', DonateView, name='donate'),
    # 技术交流
    path('category/exchange/', ExchangeView, name='exchange'),
    # 项目合作
    path('category/project/', ProjectView, name='project'),
    # 提问交流
    path('category/question/', QuestionView, name='question'),
    ]
