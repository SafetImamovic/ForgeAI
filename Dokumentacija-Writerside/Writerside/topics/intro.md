# 11.1 Ponovna Postavka Projekta

## Uvod

Ovo je ponovna implementacija projekta koji se ranije oslanjao na Supabase za autentifikaciju i bazu podataka. Sada smo odlučili ukloniti tu zavisnost i koristiti Django za backend, frontend i bazu podataka (uključujući autentifikaciju).

### Razlozi za prelazak s Supabase na Django

1. **Ograničenja Supabase-a**: Besplatni sloj Supabase-a ograničava slanje email potvrda na 3 emaila po satu. Korištenjem Google Cloud SMTP-a, taj broj može biti veći.
2. **Nezavisnost od Provajdera**: Supabase koristi AWS servere, dok ćemo mi koristiti Google Cloud direktno. Ovo nam omogućava da ne zavisimo od provajdera koji koristi cloud servis, već da direktno koristimo cloud servis bez posrednika.

## Kreiranje Projekta

### Kreiranje Root Direktora i Virtualnog Okruženja

Prvo smo kreirali novi direktorij u rootu:
```shell
mkdir ForgeAI
```

Prije kreiranja novog projekta, pokrenuli smo virtualno okruženje u Pythonu:

> Ako Python virtualno okruženje nije instalirano:
> ```shell
> pip install virtualenv
> ```

> Ovo kreira virtualno okruženje nazvano `venv` u rootu projekta:
> ```shell
> python -m venv venv
> ```

Struktura direktorija nakon kreiranja izgleda ovako:
```
/ForgeAI                  # Root repozitorija
  ├── /docs
  ├── /Dokumentacija-Writerside
  ├── /ForgeAI_django
  ├── /ForgeAI_env
  ├── /MIDI_python_parser
  ├── llama3_test.py
  ├── .env
  ├── .gitignore
  ├── README.md
  ├── instaliraj_pakete.ps1
  ├── instaliraj_pakete.sh
  ├── /ForgeAI           < + Novi direktorij
  ├── /venv              < + Novi direktorij
  │  ├── pyvenv.cfg
  │  ├── /Lib
  │  ├── /Scripts
  │  │  ├── activate.ps1 < Skripta koja aktivira virtualno okruženje
  │  ├── /Include
```

Aktivacija virtualnog okruženja iz root direktorija:
```shell
venv\Scripts\activate
```
Izlaz:
```shell
(venv) PS root
```

Provjera instaliranih paketa:
```shell
pip list
```
Izlaz:
```shell
Package    Version
---------- -------
pip        24.0
```

Deaktivacija virtualnog okruženja:
```shell
deactivate
```
Izlaz:
```shell
(venv) PS root
```
u:
```shell
PS root
```

> **Upozorenje**: Uvijek je potrebno pokrenuti virtualno okruženje prije rada na projektu.

## Postavljanje Django Projekta

### Kreiranje Django Projekta

Iz root direktorija:
```shell
cd ForgeAI
```

Pokretanje naredbe za kreiranje Django projekta:
```shell
django-admin startproject ForgeAI .
```

Ova naredba kreira osnovnu strukturu Django projekta unutar trenutnog direktorija.

Struktura nakon pokretanja komande:
```
/ForgeAI                  # Root repozitorija
  ├── /ForgeAI
  │  ├── /ForgeAI         < + Nova Direktorija
  │  │  ├── __pycache__
  │  │  ├── __init__.py
  │  │  ├── asgi.py
  │  │  ├── wsgi.py
  │  │  ├── urls.py
  │  │  ├── settings.py
  │  ├── manage.py
```


