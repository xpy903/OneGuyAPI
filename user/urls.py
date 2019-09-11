#!/usr/bin/python3
# coding: utf-8

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import AppUserView

app_name = 'user'


urlpatterns = [
    path('', csrf_exempt(AppUserView.as_view())),
]



