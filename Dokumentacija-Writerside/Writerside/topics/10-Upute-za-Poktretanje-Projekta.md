# 9. Upute za Poktretanje Projekta

Ovaj dokument pruža upute i objašnjenja za postavljanje i pokretanje Django aplikacije s integracijom Supabase baze podataka i autentifikacije, koja radi u Python virtualnom okruženju.
Napravljeno je u virtualnom okruženju radi:
- `izolacije paketa i podizanja na Docker (u budućnosti)`
- `lakšeg upravljanja paketima`
- `konfiguracijom projekta`
- `kolaboracije`

## Supabase Access Control poziv

Poslani su email-ovi:

- `sanid.muhic@gmail.com`
- `ahmedmujic123@gmail.com`

za pristup Supabase projektu. Ukoliko niste dobili poziv, kontaktirajte `safet.imamovic.22@size.ba`.
> Posto Supabase ima Access Control na nivou organizacije a ne projekta, svi korisnici će imati pristup svim projektima,
> tako da projekat `Music Streaming Service` je za predmet `Web Design` nema ništa zajedničko sa ovim projektom.

## Pokretanje Projekta

### 1. Kloniranje Git Repozitorija ili Preuzimanje Projekta

- [GitHub Repozitorij](https://github.com/SafetImamovic/ForgeAI)
- [Drive Folder Projekta](https://drive.google.com/drive/folders/1B9UPCWNuDvXVsbG7NF4GfLOaUQUKfi2M)

#### Kloniranje Repozitorija

```shell
git clone https://github.com/SafetImamovic/ForgeAI
```

#### Struktura Repozitorija

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

> **Napomena:** `.env` datoteka se ne pušta na git jer sadrži autentifikacijske ključeve i konfiguraciju baze na Supabase.

### 2. Kreiranje `.env` Datoteke

Link: [.env](https://drive.google.com/file/d/18213miLU0g_k_knuvFAcTTuy542GQH1y/view?usp=drive_link)

Kreirajte `.env` datoteku u root direktoriju projekta i popunite je sljedećim sadržajem:

```
SUPABASE_URL=https://<Supabase_url>.supabase.co
SUPABASE_KEY=<Supabase_key>
ENGINE=django.db.backends.postgresql_psycopg2
HOST=<Supabase_host>
NAME=postgres
USER=postgres.<Supabase_user>
PASSWORD=<Supabase_password>
PORT=5432
STRIPE_SECRET_KEY=<Stripe_secret_key>
STRIPE_PUBLIC_KEY=<Stripe_public_key>
STRIPE_WEBHOOK_SECRET=<Stripe_webhook_secret>
```

### 3. Aktivacija Python Virtualnog Okruženja

Nakon preuzimanja projekta, potrebno je aktivirati virtualno okruženje:

#### Aktivacija Virtualnog Okruženja

```shell
ForgeAI_env\Scripts\activate
```

Rezultat:

```
> (ForgeAI_env) PS ForgeAI:\
```

#### Deaktivacija Virtualnog Okruženja

```shell
deactivate
```

### 4. Instalacija Python Paketa

Provjerite instalirane pakete:

```shell
pip list
```

Output:

```
annotated-types     0.7.0
anyio               4.3.0
asgiref             3.8.1
certifi             2024.2.2
charset-normalizer  3.3.2
crispy-bootstrap5   2024.2
deprecation         2.1.0
Django              5.0.6
django-crispy-forms 2.1
gotrue              2.4.2
h11                 0.14.0
httpcore            1.0.5
httpx               0.27.0
idna                3.7
packaging           24.0
pip                 24.0
postgrest           0.16.4
psycopg2            2.9.9
pydantic            2.7.1
pydantic_core       2.18.2
python-dateutil     2.9.0.post0
python-dotenv       1.0.1
realtime            1.0.4
requests            2.32.2
six                 1.16.0
sniffio             1.3.1
sqlparse            0.5.0
storage3            0.7.4
StrEnum             0.4.15
stripe              9.8.0
supabase            2.4.6
supafunc            0.4.5
typing_extensions   4.12.0
tzdata              2024.1
urllib3             2.2.1
websockets          12.0
```

### 5. Pokretanje Django Servera

#### Prelazak u Direktorij s `manage.py`

```shell
cd ForgeAI_django
```

#### Pokretanje Servera

```shell
python manage.py runserver
```

Server će biti pokrenut na:

```
http://127.0.0.1:8000/
```

> **Napomena:** Ako se pojavi poruka:
> ```
> ?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace
> ```
> to znači da je dodan još jedan admin path, originalni Django middleware session admin path nije uključen.

### 6. Aktivacija Stripe Webhook Listener-a

#### Instalacija Stripe CLI

Pratite [zvaničnu dokumentaciju](https://docs.stripe.com/stripe-cli) za instalaciju Stripe CLI-a za Windows.

Preuzmite ZIP fajl za Windows s [ovog linka](https://github.com/stripe/stripe-cli/releases/tag/v1.19.5) i ekstrahujte:

`stripe_1.19.5_windows_x86_64.zip`

Postavite `stripe.exe` u stabilnu putanju, na primjer:

`C:\Stripe\stripe.exe`

#### Dodavanje Stripe CLI u Putanju Sistemskih Varijabli

U PowerShell-u s administrativnim pravima:

```shell
$env:Path += ";C:\Stripe\stripe.exe"
```

Provjerite da li je Stripe CLI dodan:

```shell
$env:Path
```

Provjerite verziju Stripe-a:

```shell
stripe --version
```

#### Autentifikacija Stripe CLI

U drugom terminal prozoru:

```shell
stripe login
```

Prijavite se s vašim Stripe računom.

#### Pokretanje Webhook Listener-a

```shell
stripe listen --forward-to localhost:8000/collect-stripe-webhook/
```

Odgovor:

```
> Ready! You are using Stripe API Version [2024-04-10]. Your webhook signing secret is <Secret Key> (^C to quit)
```

### 7. Pristup Početnoj Stranici

Kada su Django server i Stripe webhook pokrenuti, početna stranica se nalazi na:

```
http://127.0.0.1:8000/home
```

> **Napomena:** Početni path: 
> ```
>http://127.0.0.1:8000/
>```
> Ne sadrži nikakav sadržaj pa će dati error.


To su upute za kloniranje i postavljanje projekta.