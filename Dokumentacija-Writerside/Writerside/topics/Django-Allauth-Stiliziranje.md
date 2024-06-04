# Django Allauth Stiliziranje

## Allauth Šablonski Sistemi

`Allauth` nudi podrazumijevane šablone za prikaze autentifikacije korisnika (prijava, registracija itd.) ali su oni **obični** i **bez stila**.

Postoje dva načina za prilagođavanje izgleda i dojma:

- Kopiranje svih šablona u projekat i njihovo individualno stiliziranje. Ovo daje najviše kontrole, ali može biti nezgodno za složene postavke.

- Zamjena nekoliko centralnih šablona koji kontroliraju opći raspored i stilove elemenata. Ovo je brže, ali manje fleksibilno.

**Glavni šabloni** uključuju rasporede:
   

| bazni       | ulazni              | upravljanje nalogom |
|-------------|---------------------|---------------------|
| `base.html` | `entrance.html`     | `manage.html`       |


> Ovi šabloni se mogu pronaći u direktoriju `ForgeAI (root)/venv/Lib/allauth/templates/allauth/layouts` u `allauth` paketu.
> {style="note"}

```
ForgeAI (root)
└── ForgeAI
    ├── ForgeAI
    ├── static
    │   ├── allauth_ui
    │   │   └── input.css
    │   └── css
    │       └── global.css
    ├── templates
    │   ├── account
    │   │   ├── email
    │   │   │   ├── email_confirmation_message.txt
    │   │   │   └── email_confirmation_subject.txt
    │   │   ├── messages
    │   │   │   ├── cannot_delete_primary_email.txt
    │   │   │   ├── email_confirmation_failed.txt
    │   │   │   ├── email_confirmation_sent.txt
    │   │   │   ├── email_confirmed.txt
    │   │   │   ├── email_deleted.txt
    │   │   │   ├── logged_in.txt
    │   │   │   ├── logged_out.txt
    │   │   │   ├── login_code_sent.txt
    │   │   │   ├── password_changed.txt
    │   │   │   ├── password_set.txt
    │   │   │   ├── primary_email_set.txt
    │   │   │   └── unverified_primary_email.txt
    │   │   ├── snippets
    │   │   │   ├── already_logged_in.html
    │   │   │   └── warn_no_email.html
    │   │   ├── account_inactive.html
    │   │   ├── base_entrance.html
    │   │   ├── base_manage_email.html
    │   │   ├── base_manage_password.html
    │   │   ├── base_manage.html
    │   │   ├── base_reauthenticate.html
    │   │   ├── base.html
    │   │   ├── confirm_login_code.html
    │   │   ├── email_change.html
    │   │   ├── email_confirm.html
    │   │   ├── email.html
    │   │   ├── login.html
    │   │   ├── logout.html
    │   │   ├── password_change.html
    │   │   ├── password_reset_done.html
    │   │   ├── password_reset_from_key_done.html
    │   │   ├── password_reset_from_key.html
    │   │   ├── password_reset.html
    │   │   ├── password_set.html
    │   │   ├── reauthenticate.html
    │   │   ├── request_login_code.html
    │   │   ├── signup_closed.html
    │   │   ├── signup.html
    │   │   ├── verification_sent.html
    │   │   └── verified_email_required.html
    │   ├── admin
    │   │   └── base_site.html
    │   ├── allauth
    │   │   ├── elements
    │   │   │   ├── alert.html
    │   │   │   ├── badge.html
    │   │   │   ├── button.html
    │   │   │   ├── field.html
    │   │   │   ├── fields.html
    │   │   │   ├── form.html
    │   │   │   ├── h1.html
    │   │   │   ├── h2.html
    │   │   │   ├── hr.html
    │   │   │   ├── img.html
    │   │   │   ├── p.html
    │   │   │   ├── panel.html
    │   │   │   ├── provider_list.html
    │   │   │   ├── provider.html
    │   │   │   └── table.html
    │   │   └── layouts
    │   │       ├── base.html
    │   │       ├── entrance.html
    │   │       └── manage.html
    │   ├── mfa
    │   │   ├── email
    │   │   │   ├── recovery_codes_generated_message.txt
    │   │   │   ├── recovery_codes_generated_subject.txt
    │   │   │   ├── totp_activated_message.txt
    │   │   │   ├── totp_activated_subject.txt
    │   │   │   ├── totp_deactivated_message.txt
    │   │   │   └── totp_deactivated_subject.txt
    │   │   ├── messages
    │   │   │   ├── recovery_codes_generated.txt
    │   │   │   ├── totp_activated.txt
    │   │   │   └── totp_deactivated.txt
    │   │   ├── recovery_codes
    │   │   │   ├── base.html
    │   │   │   ├── download.txt
    │   │   │   ├── generate.html
    │   │   │   └── index.html
    │   │   ├── totp
    │   │   │   ├── activate_form.html
    │   │   │   ├── base.html
    │   │   │   └── deactivate_form.html
    │   │   ├── authenticate.html
    │   │   ├── base_entrance.html
    │   │   ├── base_manage.html
    │   │   ├── index.html
    │   │   └── reauthenticate.html
    │   └── socialaccount
    │       ├── snippets
    │       │   ├── provider_list.html
    │       │   └── social_login.html
    │       ├── authentication_error.html
    │       ├── base.html
    │       ├── connections.html
    │       ├── login.html
    │       └── signup.html
```
{collapsible="true" collapsed-title="Struktura Direktorija nakon kopiranja šablona"}

<tabs>
<tab title="base.html">
    <code-block lang="python" collapsible="true" collapsed-title="base.html" src="base_ref.html" />
</tab>
<tab title="entrance.html">
    <code-block lang="python" collapsible="true" collapsed-title="entrance.html">
        <![CDATA[
            {% extends "allauth/layouts/base.html" %}
            {% block content %}{% endblock %}
        ]]>
    </code-block>
</tab>
<tab title="manage.html">
<code-block lang="python" collapsible="true" collapsed-title="manage.html">
        <![CDATA[
            {% extends "allauth/layouts/base.html" %}
            {% block content %}{% endblock %}
        ]]>
    </code-block>
</tab>
</tabs>

## Globalni CSS

Globalni CSS fajl se može koristiti za stiliziranje elemenata na svim stranicama. Ovaj fajl: `global.css` se nalazi u direktorij `ForgeAI (root)/static/css` i uključuje u `base.html` šablon.

<code-block lang="css" src="global.css" />

## Kopiranje i Modifikacija Šablona

i šablone elemenata (zaglavlja, tipke, obrasci itd.). Zamjenom ovih šablona elemenata, može promijeniti stilove na svim stranicama bez modifikacije sadržaja.

<tabs>
<tab title="Originalni base.html u paketu">
<code-block lang="html" src="base_ref.html" collapsible="true"/>
</tab>
<tab title="Kopirani i modificirani base.html">
<code-block lang="html" src="base.html" collapsible="true"/>
</tab>
</tabs>

Link za [`Django Allauth` Dokumentaciju za Templates](https://docs.allauth.org/en/latest/common/templates.html)

## Modifikacija kod `html` elemenata

Radi lakšeg stiliziranja auth stranica koje koriste `allauth`, okolo svakog elementa se može dodati `div` sa klasom `auth-element` koja će omogućiti lakše stiliziranje elemenata.

primjer kod `signup.html`:

<compare>
<code-block lang="html" src="signup_ref.html" collapsible="true"/>
<code-block lang="html" src="signup.html" collapsible="true"/>
</compare>

> Potrebno je uočiti kako je dodan
> ```
> <div class="auth-element">
> ...
> </div>
> ```
{style="note"}

## Dizajn Stranica
Svaka stranica ima `.nav-bar` <shortcut>CSS</shorcut> klasu koja se može koristiti za stiliziranje navigacijske trake (nalazi se u `base.html`).

> Ne smije se mijenjati `base.html` pod `allauth` paketom jer će se promjene izgubiti prilikom ažuriranja paketa.
{style="warning"}

> Smije se mijenjati `base.html` pod `templates` direktorijem (koji se nalazi pod ForgeAI) jer se ovi šabloni koriste prije šablona iz `allauth` paketa.
{style="note"}

<procedure title="Procedura Stiliziranja" id="procedura_stiliziranja">
<step>Ako se želi promijeniti stil globalno, dovoljno je promijeniti <code>global.css</code> fajl.</step>

<step>Kako je definiran <code>auth-element</code> u <code>global.css</code> fajlu, svi elementi koji imaju ovu klasu će biti stilizirani prema definiciji u ovom fajlu (to su auth stranice). Ako se želi promijeniti stil, dovoljno je promijeniti <code>global.css</code> fajl i <code>style tag</code> unutar <code>base.html</code>. </step>

<step>Ako se želi promijeniti stil samo jednog elementa, npr. <code>signup.html</code>, dovoljno je promijeniti <code>signup.html</code> fajl.</step>
</procedure>
