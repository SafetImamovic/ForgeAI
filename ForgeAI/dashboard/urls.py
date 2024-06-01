from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('my-products/', views.my_products, name='my_products'),
]
