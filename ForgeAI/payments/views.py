import os
import json
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe
from django.contrib.auth import login
from django.contrib.auth.models import User
from . import models

DOMAIN = "http://localhost:8000"  # Move this to your settings file or environment variable for production.
stripe.api_key = os.environ['STRIPE_SECRET_KEY']

def subscribe(request) -> HttpResponse:
    # We login a sample user for the demo.
    if not request.user.is_authenticated:
        return redirect('account_login')

    return render(request, 'subscribe.html')

def cancel(request) -> HttpResponse:
    return render(request, 'cancel.html')

def success(request) -> HttpResponse:
    print(f'{request.session = }')
    stripe_checkout_session_id = request.GET['session_id']
    return render(request, 'success.html')

def create_checkout_session(request) -> HttpResponse:
    price_lookup_key = request.POST['price_lookup_key']
    try:
        prices = stripe.Price.list(lookup_keys=[price_lookup_key], expand=['data.product'])
        price_item = prices.data[0]

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {'price': price_item.id, 'quantity': 1},
                # You could add differently priced services here, e.g., standard, business, first-class.
            ],
            mode='subscription',
            success_url=DOMAIN + reverse('success') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=DOMAIN + reverse('cancel')
        )
        
        models.CheckoutSessionRecord.objects.create(
            user=request.user,
            stripe_checkout_session_id=checkout_session.id,
            stripe_price_id=price_item.id,
            product_name='ForgeAI PRO',
            product_description='ForgeAI PRO MIDI Generator'
        )

        return redirect(
            checkout_session.url,  # Either the success or cancel url.
            code=303
        )
    except Exception as e:
        print(e)
        return HttpResponse("Server error", status=500)

def direct_to_customer_portal(request) -> HttpResponse:
    checkout_record = models.CheckoutSessionRecord.objects.filter(
        user=request.user
    ).last()

    checkout_session = stripe.checkout.Session.retrieve(checkout_record.stripe_checkout_session_id)

    portal_session = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=DOMAIN + reverse('my_products')
    )
    return redirect(portal_session.url, code=303)


@csrf_exempt
def collect_stripe_webhook(request) -> JsonResponse:
    webhook_secret = os.environ.get('STRIPE_WEBHOOK_SECRET')
    signature = request.META["HTTP_STRIPE_SIGNATURE"]
    payload = request.body

    try:
        event = stripe.Webhook.construct_event(
            payload=payload, sig_header=signature, secret=webhook_secret
        )
    except ValueError as e:  # Invalid payload.
        raise ValueError(e)
    except stripe.error.SignatureVerificationError as e:  # Invalid signature
        raise stripe.error.SignatureVerificationError(e)

    _update_record(event)

    return JsonResponse({'status': 'success'})


def _update_record(webhook_event) -> None:
    data_object = webhook_event['data']['object']
    event_type = webhook_event['type']

    if event_type == 'checkout.session.completed':
        checkout_record = models.CheckoutSessionRecord.objects.get(
            stripe_checkout_session_id=data_object['id']
        )
        checkout_record.stripe_customer_id = data_object['customer']
        checkout_record.has_access = True
        checkout_record.save()
        print('🔔 Payment succeeded!')
    elif event_type == 'customer.subscription.created':
        print('🎟️ Subscription created')
    elif event_type == 'customer.subscription.updated':
        print('✍️ Subscription updated')
    elif event_type == 'customer.subscription.deleted':
        checkout_record = models.CheckoutSessionRecord.objects.get(
            stripe_customer_id=data_object['customer']
        )
        checkout_record.has_access = False
        checkout_record.save()
        print('✋ Subscription canceled: %s', data_object.id)
