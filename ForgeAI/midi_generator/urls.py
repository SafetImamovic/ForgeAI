from django.urls import path, include
from midi_generator import views

urlpatterns = [
    path('', views.sessions, name='sessions'),

]
