from django.contrib import admin
from django.urls import path, include
from stripe_pretplata import views

urlpatterns = [
    path('pretplati/', views.subscribe, name='pretplati'),
    path('otkazi/', views.cancel, name='otkazi'),
    path('uspjeh/', views.success, name='uspjeh'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('direct-to-customer-portal/', views.direct_to_customer_portal, name='direct-to-customer-portal'),
    path('collect-stripe-webhook/', views.collect_stripe_webhook, name='collect-stripe-webhook'),
]