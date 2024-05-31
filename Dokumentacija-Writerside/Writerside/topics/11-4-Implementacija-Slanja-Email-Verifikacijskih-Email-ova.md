# 11.4 Implementacija Slanja Verifikacijskih Email-ova

## Korak 1: Konfiguracija Email Verifikacije u `settings.py`

U `settings.py` fajlu unutar Django projekta, konfigurišemo slanje email verifikacijskih email-ova.

```
/ForgeAI                    # root repozitorija
    ├── /ForgeAI
    │   ├── /ForgeAI
    │   │   ├── settings.py	< -
```

U ovom fajlu mijenjamo određene postavke kako bismo omogućili email verifikaciju.

```python
# Postavka za obaveznu email verifikaciju
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
```

Ova postavka će natjerati svakog novog korisnika da verifikuje svoj email prije nego što se može prijaviti.

## Korak 2: Konfiguracija Gmail SMTP-a za Slanje Email-ova

Koristimo Gmail SMTP (Simple Mail Transfer Protocol) za slanje email adresa za verifikaciju korisnika. Prvo, unutar `settings.py` fajla, definišemo neophodne postavke za Gmail SMTP.

Da bismo zaštitili osjetljive informacije kao što su korisničko ime i lozinka za pristup Gmail SMTP-u, koristimo `.env` file.

```shell
pip install python-dotenv
```

Sada možemo dodati `.env` file na istom nivou kao i `settings.py`.

```
/ForgeAI                    # root repozitorija
    ├── /ForgeAI
    │   ├── /ForgeAI
    │   │   ├── settings.py
    │   │   ├── .env	< +
```

```python
import os
from dotenv import load_dotenv

load_dotenv()
```

Zatim definišemo postavke za Gmail SMTP koristeći podatke iz `.env` file-a.

```python
...
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True').lower() == 'true'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
...
```

## Korak 3: Kreiranje Django App-a za Homepage

Napravljen je novi Django app koji će služiti kao homepage, ali će biti korišten i za druge stranice, ne samo za homepage.

```
/ForgeAI                    # root repozitorija
    ├── /ForgeAI
    │   ├── /ForgeAI
    │   ├── /homepage
    │   │   ├── /templates
    │   │   │   ├── /homepage
    │   │   │   │   ├── homepage.html
    │   │   ├── /static
    │   │   │   ├── /css
    │   │   │   │   ├── styles.css
```

U `homepage.html` fajlu definišemo strukturu i sadržaj homepage-a.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
    {% load static %} <!-- Učitavanje statičke biblioteke -->
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <h1>Welcome to the Homepage</h1>
    <p>This is a sample homepage styled with CSS.</p>
</body>
</html>
```

Ovaj HTML kod predstavlja jednostavnu strukturu homepage-a sa minimalnim CSS stilizovanjem.

## Završne Napomene

- Nakon implementacije ovih koraka, aplikacija će moći slati email-ove za verifikaciju korisnika putem Gmail SMTP-a.
- Homepage je kreiran kao Django app i definisani su HTML i CSS fajlovi koji čine strukturu i izgled homepage-a.
