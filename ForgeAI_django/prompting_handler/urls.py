from django.contrib import admin
from django.urls import path
from prompting_handler import views

urlpatterns = [
    path('', views.index, name='index'),
    path('session/<int:session_id>/', views.chat_session, name='chat_session'),
    path('create/', views.create_session, name='create_session'),
]
