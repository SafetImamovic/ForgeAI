import os
import json
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import stripe
from django.contrib.auth import login
from django.contrib.auth.models import User
from . import models
from ForgeAI_django import settings

DOMAIN = "http://localhost:8000"
stripe.api_key = os.environ['STRIPE_SECRET_KEY']

def subscribe(request) -> HttpResponse:
    user_live = request.session.get('user')
    if not user_live:
        return redirect('login')
    
    response_s = settings.supabase.table('stripe_pretplata_checkoutsesijazapis').select('*').eq('user_uuid', user_live['id']).execute();
    
    if (len(response_s.data) > 0):
        checkout_record = models.CheckoutSesijaZapis.objects.get(
                user_uuid=user_live['id']
            )
    
        if (checkout_record.ima_pristup == True):
            return redirect('home')

    return render(request, 'pretplati.html')


def cancel(request) -> HttpResponse:
    return render(request, 'otkazi.html')


def success(request) -> HttpResponse:

    print(f'{request.session = }')

    stripe_checkout_session_id = request.GET['session_id']

    return render(request, 'uspjeh.html')


def create_checkout_session(request) -> HttpResponse:
    user_live = request.session.get('user')
    if not user_live:
        return redirect('login')
    
    
    
    price_lookup_key = request.POST['price_lookup_key']
    #try:
    prices = stripe.Price.list(lookup_keys=[price_lookup_key], expand=['data.product'])
    price_item = prices.data[0]

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {'price': price_item.id, 'quantity': 1},
            
        ],
        mode='subscription',
        success_url=DOMAIN + reverse('uspjeh') + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=DOMAIN + reverse('otkazi')
    )
    
    # We connect the checkout session to the user who initiated the checkout.
    models.CheckoutSesijaZapis.objects.create(
        user_uuid=user_live['id'],
        stripe_checkout_session_id=checkout_session.id,
        stripe_cijena_id=price_item.id,
    )

    return redirect(
        checkout_session.url,  # Either the success or cancel url.
        code=303
    )
    # except Exception as e:
    #     print(e)
    #     return HttpResponse("Server error", status=500)


def direct_to_customer_portal(request) -> HttpResponse:
    user_live = request.session.get('user')
    if not user_live:
        return redirect('login')
    
    checkout_record = models.CheckoutSesijaZapis.objects.filter(
        user_uuid=user_live['id']
    ).last()  # For demo purposes, we get the last checkout session record the user created.

    checkout_session = stripe.checkout.Session.retrieve(checkout_record.stripe_checkout_session_id)

    portal_session = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=DOMAIN + reverse('pretplati')  # Send the user here from the portal.
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
        checkout_record = models.CheckoutSesijaZapis.objects.get(
            stripe_checkout_session_id=data_object['id']
        )
        checkout_record.stripe_kupac_id = data_object['customer']
        checkout_record.ima_pristup = True
        checkout_record.save()
        print('🔔 Payment succeeded!')
    elif event_type == 'customer.subscription.created':
        print('🎟️ Subscription created')
    elif event_type == 'customer.subscription.updated':
        print('✍️ Subscription updated')
    elif event_type == 'customer.subscription.deleted':
        checkout_record = models.CheckoutSesijaZapis.objects.get(
            stripe_kupac_id=data_object['customer']
        )
        checkout_record.ima_pristup = False
        checkout_record.save()
        print('✋ Subscription canceled: %s', data_object.id)

