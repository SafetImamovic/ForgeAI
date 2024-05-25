from django.contrib import admin
from django.urls import path
from backend_logika import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home')
]
