# This file is importing urls from urls.py from core folder.
"""This is going to show urls/views imported from core/urls.py 
"""
from django.urls import path, include
from . import views

# All these are urls posted.
urlpatterns = [
   path("home/", views.home),
]
