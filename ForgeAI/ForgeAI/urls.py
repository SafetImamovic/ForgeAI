from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('dashboard.urls')),
    path('', include('homepage.urls')),
    path('payments/', include('payments.urls')),
    path('midi-generator/', include('midi_generator.urls')),
    path('chatbot/', include('chatbot.urls')),
]
