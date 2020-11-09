from django.contrib import admin
from django.urls import path, include

from wwwKot.views import index

urlpatterns = [
    path('', index),
]
