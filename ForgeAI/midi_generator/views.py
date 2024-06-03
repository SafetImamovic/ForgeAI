from django.shortcuts import render, redirect
from payments import models
from payments.models import CheckoutSessionRecord
from django.http import JsonResponse


def sessions(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    try:
        record = CheckoutSessionRecord.objects.get(user=request.user)
    except CheckoutSessionRecord.DoesNotExist:
        return redirect('subscribe')
    
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'Hello'
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'sessions.html', context={'record': record})
