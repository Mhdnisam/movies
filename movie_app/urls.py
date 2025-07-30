from django.contrib import admin
from django.urls import path

from movie_app import views

urlpatterns = [
    path('hello/', views.hello),
]
