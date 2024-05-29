# 10.3 Implementacija Stripe-a

## Struktura Projekta

```
/ForgeAI                    # root repozitorija
    ├── /docs
    ├── /Dokumentacija-Writerside
    ├── /ForgeAI_django
    │   ├── manage.py
    │   ├── /ForgeAI_django
    │   │   ├── __pycache__
    │   │   ├── __init__.py
    │   │   ├── asgi.py
    │   │   ├── wsgi.py
    │   │   ├── urls.py
    │   │   ├── settings.py
    │   ├── __pycache__
    │   ├── /backend_logika
    │   ├── /prompting_handler
    │   ├── /stripe_pretplata
    │   ├── Korisnik.py
    ├── /ForgeAI_env
    │   ├── /Scripts
    │   │   ├── activate.bat
    ├── /MIDI_python_parser
    │   ├── chords.py
    │   ├── custom_midi_gen.py
    │   ├── drums.py
    │   ├── main.py
    │   ├── midi_to_format.py
    ├── llama3_test.py
    ├── .env
    ├── .gitignore
    ├── README.md
```

## Kreiranje Aplikacije

```shell
python manage.py startapp stripe_pretplata
```

Ova komanda kreira novu Django aplikaciju pod nazivom `stripe_pretplata`.

## Dodavanje Aplikacije u settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend_logika',
    'prompting_handler',
    'stripe_pretplata'
]
```

Ovdje se dodaje `stripe_pretplata` aplikacija u listu instaliranih aplikacija u `settings.py` datoteci.

## Instalacija Stripe Paketa

```shell
pip install stripe
```

Ova komanda instalira Stripe paket koji ćemo koristiti za integraciju plaćanja. Važno je napomenuti da se ovo pokreće unutar Python virtualnog okruženja.

## Kreiranje Produkta na Stripe Dashboard-u

1. **Dodavanje novog produkta**: U sekciji Product Catalogue dodajemo novi produkt.
2. **Postavljanje jedinstvenog ključa za cijenu**: Ključ za cijenu mora biti jedinstven jer se koristi u kodu za kasnije pretraživanje.
3. **Aktivacija Stripe Customer Portala**: Omogućava korisnicima da upravljaju svojim pretplatama putem Stripe-ovog korisničkog portala.

### Stripe CLI

Instalacija Stripe CLI-a prema zvaničnoj dokumentaciji: [Stripe CLI Dokumentacija](https://docs.stripe.com/stripe-cli)

Preuzimanje Stripe CLI za Windows: [Stripe CLI za Windows](https://github.com/stripe/stripe-cli/releases/tag/v1.19.5)

Ekstraktovanje i postavljanje `stripe.exe` u `C:\Stripe` direktorij. Dodavanje `stripe.exe` u `Path` varijablu okruženja:

```shell
$env:Path += ";C:\Stripe\stripe.exe"
```

Provjera Stripe CLI verzije:

```shell
stripe --version
```

## Konfiguracija .env Datoteke

U `.env` datoteku dodajemo Stripe API ključeve:

```
STRIPE_SECRET_KEY=<sk_test_51>
STRIPE_PUBLIC_KEY=<pk_test_51>
STRIPE_WEBHOOK_SECRET=<whsec_51>
```

## Kreiranje Tabela u Bazi Podataka

U ovoj sekciji ćemo opisati tabele koje se kreiraju u bazi podataka:

### Tabela `users`

Sadrži podatke o korisnicima, uključujući njihovo ime, avatar URL, adresu za naplatu i metode plaćanja.

### Tabela `customers`

Privatna tabela koja sadrži mapiranje korisničkih ID-ova na Stripe ID-ove.

### Tabela `products`

Sadrži informacije o proizvodima kreiranim i upravljanim u Stripe-u.

### Tabela `prices`

Sadrži informacije o cijenama proizvoda, uključujući tip cijene i interval naplate.

### Tabela `subscriptions`

Sadrži informacije o pretplatama korisnika, uključujući status, ID cijene i vremenske oznake.

---

## Dodavanje Templates Direktorija u Aplikaciju

Unutar aplikacije `stripe_pretplata` kreiramo novi `templates` direktorij i dodajemo sljedeće HTML datoteke:

- `pretplati.html`
- `uspjeh.html`
- `otkazi.html`

### `pretplati.html` Boilerplate

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Subscribe to a cool new product</title>
    <script src="https://js.stripe.com/v3/"></script>
  </head>
  <body>
    <header>
        <p>
            Logged in as {{ request.user.email }}
        </p>
    </header>
    <section>
      <div class="product">
        <div class="description">
          <h3>Starter - Monthly tennis ball delivery 🎾</h3>
          <h5>$20.00 / month</h5>
        </div>
      </div>
      <form class="checkout-form" action="{%  url 'create-checkout-session' %}" method="POST">
          {% csrf_token %}
        <input type="hidden" name="price_lookup_key" value="standard_monthly" />
        <button id="checkout-and-portal-button" type="submit">Checkout</button>
      </form>
    </section>
  </body>
</html>
<style>
    .product {
        display: flex;
        justify-content: center;
        padding: 20px 10px;
        border: 1px dashed lightgreen;
    }
    .checkout-form {
        display: flex;
        justify-content: center;
        padding: 20px 10px;
    }
</style>
```

### `uspjeh.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Thanks for your order!</title>
  <link rel="stylesheet" href="style.css">
  <script src="client.js" defer></script>
</head>
<body>
  <section>
    <div class="product Box-root">
      <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="14px" height="16px" viewBox="0 0 14 16" version="1.1">
          <defs/>
          <g id="Flow" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g id="0-Default" transform="translate(-121.000000, -40.000000)" fill="#E184DF">
                  <path d="M127,50 L126,50 C123.238576,50 121,47.7614237 121,45 C121,42.2385763 123.238576,40 126,40 L135,40 L135,56 L133,56 L133,42 L129,42 L129,56 L127,56 L127,50 Z M127,48 L127,42 L126,42 C124.343146,42 123,43.3431458 123,45 C123,46.6568542 124.343146,48 126,48 L127,48 Z" id="Pilcrow"/>
              </g>
          </g>
      </svg>
      <div class="description Box-root">
        <h3>Subscription to Starter plan successful!</h3>
      </div>
    </div>
      <div> User = {{request.user}} </div>
    <form action="{%  url  'direct-to-customer-portal' %}" method="POST">
        {% csrf_token %}
      <input type="hidden" id="session-id" name="session_id" value="" />
      <button id="checkout-and-portal-button" type="submit">Manage your billing information</button>
    </form>
  </section>
</body>
</html>
```

### `otkazi.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Checkout canceled</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <section>
    <p>Picked the wrong subscription? Shop around then come back to pay!</p>
  </section>
</body>
</html>
```

## Dodavanje Koda u `views.py`

U `views.py` dodajemo funkcije za upravljanje pretplatama, uključujući kreiranje sesija za naplatu, upravljanje korisničkim portalom i obradu webhook događaja. Ovdje su najvažniji dijelovi koda:

- `subscribe`: Funkcija koja prikazuje stranicu za pretplatu.
- `cancel`: Funkcija koja prikazuje stranicu za otkazivanje.
- `success`: Funkcija koja prikazuje stranicu za uspješ

nu pretplatu.
- `create_checkout_session`: Funkcija koja kreira novu sesiju za naplatu koristeći Stripe API.
- `direct_to_customer_portal`: Funkcija koja preusmjerava korisnika na Stripe korisnički portal.

### `views.py` - Primjer Koda

```python
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

def subscribe(request):
    return render(request, 'stripe_pretplata/pretplati.html')

def cancel(request):
    return render(request, 'stripe_pretplata/otkazi.html')

def success(request):
    return render(request, 'stripe_pretplata/uspjeh.html')

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        domain_url = 'http://localhost:8000/'
        price_lookup_key = request.POST['price_lookup_key']
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Starter Subscription',
                            },
                            'unit_amount': 2000,
                            'recurring': {
                                'interval': 'month',
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=domain_url + 'stripe_pretplata/uspjeh.html',
                cancel_url=domain_url + 'stripe_pretplata/otkazi.html',
            )
            return JsonResponse({
                'id': checkout_session.id
            })
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            })
```

## Kreiranje URL Mappings u `urls.py`

U `urls.py` datoteci dodajemo URL mappings za nove funkcije:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('pretplati/', views.subscribe, name='pretplati'),
    path('otkazi/', views.cancel, name='otkazi'),
    path('uspjeh/', views.success, name='uspjeh'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('direct-to-customer-portal/', views.direct_to_customer_portal, name='direct-to-customer-portal'),
]
```
