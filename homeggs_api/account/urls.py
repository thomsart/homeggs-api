"""
Module for account urls
"""

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserLogin, UserLogout


app_name = 'account'

urlpatterns = [
    path('' , include('djoser.urls')),
    path('' , include('djoser.urls.authtoken')),
    path('' , include('djoser.urls.jwt')),
]