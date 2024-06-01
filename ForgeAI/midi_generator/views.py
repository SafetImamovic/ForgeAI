from django.shortcuts import render, redirect
from payments import models
from payments.models import CheckoutSessionRecord

def sessions(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    try:
        record = CheckoutSessionRecord.objects.get(user=request.user)
    except CheckoutSessionRecord.DoesNotExist:
        return redirect('subscribe')

    return render(request, 'sessions.html', context={'record': record})
