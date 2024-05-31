# 11.2 Instalacija i Konfiguracija Django Allauth

Sljedeća komanda instalira Django Allauth paket:
```shell
pip install django-allauth
```

Potrebne izmjene u `settings.py` kako bi Allauth radio:

**Dodavanje autentifikacijskih backend-ova:**
```python
AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'allauth.account.auth_backends.AuthenticationBackend'
]
```

**Dodavanje aplikacija u `INSTALLED_APPS`:**
```python
INSTALLED_APPS = [
  'allauth',
  'allauth.account',
  'allauth.socialaccount',
  ...
]
```

**Dodavanje middleware-a:**
```python
MIDDLEWARE = [
  ...
  'allauth.account.middleware.AccountMiddleware'
]
```

**Dodatne postavke za Allauth:**
```python
SOCIALACCOUNT_PROVIDERS = {}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True
```

## Dodavanje URL-ova za Allauth

Izmjene u `urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/', include('allauth.urls')),
]
```
Ova naredba uključuje URL-ove za Allauth autentifikaciju.

### Primjena Migracija

Pokretanje migracija:
```shell
python manage.py migrate
```
Ova komanda primjenjuje sve migracije i kreira bazu podataka.

Struktura nakon migracije:
```
/ForgeAI                  # Root repozitorija
  ├── /ForgeAI
  │  ├── manage.py
  │  ├── db.sqlite3       < + Nova baza podataka ⛁
```

## Kreiranje Superusera

Pokretanje komande za kreiranje superusera:
```shell
python manage.py createsuperuser

> Username: admin
> Email address: safet.imamovic.22@size.ba
> Password: 
> Password (again): 
Superuser created successfully.
```

## Pokretanje Servera

Pokretanje razvojnog servera:
```shell
python manage.py runserver
```

Izlaz:
```shell
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 31, 2024 - 13:43:57
Django version 5.0.6, using settings 'ForgeAI.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

> **Upozorenje**: Pošto nema `index.html` stranice, dobit će se 404 error "Not Found". Međutim, na `http://127.0.0.1:8000/admin` postoji admin login stranica.

### Primjer Registracije Novog Accounta

Registracija novog korisnika na `http://127.0.0.1:8000/accounts/signup/`:

Primjer testnog accounta:
- **Email**: test@test.com
- **Username**: test
- **Password**: test1234@@

Prikaz email potvrde u konzoli:
```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: [127.0.0.1:8000] Please Confirm Your Email Address
From: webmaster@localhost
To: test@test.com
Date: Fri, 31 May 2024 11:50:45 -0000
Message-ID: <171715624535.14724.8192548555147862071@DESKTOP-24UA1HK.local>

Hello from 127.0.0.1:8000!

You're receiving this email because user test has given your email address to register an account on 127.0.0.1:8000.

To confirm this is correct, go to http://127.0.0.1:8000/accounts/confirm-email/Mg:1sD0mT:xoP-4Ts5ikiXEIAAK6KANr77ERX-m8gMfJLfR_fwzuU/

Thank you for using 127.0.0.1:8000!
127.0.0.1:8000
```

## Kreiranje Aplikacije za Dashboard

Napravljena je nova aplikacija:
```shell
python manage.py startapp dashboard
```

Nakon kreiranja dodana je direktorija `templates` i u njoj `profile.html`:
```
/ForgeAI                  # Root repozitorija
  ├── /ForgeAI
  │  ├── /ForgeAI
  │  ├── /dashboard       < + Nova Direktorija
  │  │  ├── /templates    < + Nova Direktorija
  │  │  │  ├── profile.html < + Novi file
  │  ├── manage.py
  │  ├── db.sqlite3 ⛁
```

Dodavanje aplikacije u `settings.py`:
```python
INSTALLED_APPS = [


  'dashboard',
  ...
]
```

Dodavanje pogleda u `views.py`:
```python
from django.shortcuts import render

def profile(request):
  return render(request, 'profile.html')
```

Sadržaj `profile.html`:
```html
<h1>Logged in kao: {{ request.user.username }}</h1>

<a href="{% url 'account_logout' %}">Logout</a>
```

Dodavanje rute u `urls.py`:
```python
urlpatterns = [
  ...
  path('accounts/profile/', views.profile, name='profile')
]
```