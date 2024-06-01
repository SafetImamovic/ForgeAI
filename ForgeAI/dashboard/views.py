from django.shortcuts import render, redirect
from payments.models import CheckoutSessionRecord
import stripe

def profile(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    
    return render(request, 'profile.html')

def my_products(request):
    if not request.user.is_authenticated:
        return redirect('account_login')

    records = CheckoutSessionRecord.objects.filter(user=request.user)

    if not records.exists():
        # No records found, handle it in the template
        return render(request, 'my_products.html', context={'records': []})

    try:
        product = stripe.Product.retrieve(records[0].stripe_price_id)
        records[0].product_name = product.name
        records[0].product_description = product.description
    except stripe.error.StripeError:
        print('Error')

    return render(request, 'my_products.html', context={'records': [records[0]]})


