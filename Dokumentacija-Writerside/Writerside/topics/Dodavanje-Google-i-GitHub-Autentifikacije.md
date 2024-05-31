# 11.3 Dodavanje Google i GitHub Autentifikacije

Instalacija potrebnih paketa:
```shell
pip install "django-allauth[socialaccount]"
```

Dodavanje aplikacija u `settings.py`:
```python
INSTALLED_APPS = [
  ...
  'allauth.socialaccount.providers.google',
  'allauth.socialaccount.providers.github',
  ...
]
```

![](../../images/Auth/1.png)

![](../../images/Auth/2.png)

![](../../images/Auth/3.png)

Kroz admin dashboard se može uspostaviti autentifikacija putem Google i GitHub providera.

![](../../images/Auth/4.png)

![](../../images/Auth/5.png)

![](../../images/Auth/6.png)

## Dokumentacija za Allauth

[Allauth Dokumentacija](https://docs.allauth.org/en/dev/socialaccount/index.html)

> Unutar `/venv` direktorija nalaze se templates za Allauth stranice:
```
/ForgeAI                  # Root repozitorija
  ├── /venv
  │  ├── pyvenv.cfg
  │  ├── /Lib
  │  │  ├── /allauth
  │  │  │  ├── /templates
  │  │  │  │  ├── (HTML Templates)
```

Templates se mogu stilizirati na osnovu [ove dokumentacije](https://docs.allauth.org/en/latest/common/templates.html).
