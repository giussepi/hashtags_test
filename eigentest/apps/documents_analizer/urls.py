# -*- coding: utf-8 -*-
""" apps documents_analizer urls """

from django.urls import path

from . import views

app_name = 'documents_analizer'
urlpatterns = [
    path('', views.HashtagsView.as_view(), name='home'),
]
