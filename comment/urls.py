# -*- coding: utf-8 -*-
from .views import AddcommentView
from django.contrib import admin
from django.urls import path, include,re_path
urlpatterns = [
   re_path(r'^add/$', AddcommentView, name='add_comment'),
        ]


