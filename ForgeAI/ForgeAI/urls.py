from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name='profile')
]
