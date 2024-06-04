# Google Cloud

## Implementacija Google Cloud Generative Language API

`Google Cloud` nudi `Generative Language`<shortcut>API</shortcut> koji omogućava programerima izradu aplikacija **generativne umjetne inteligencije** koristeći `Gemini` modele. Ovi modeli su **multimodalni**, što znači da mogu razumjeti i kombinirati različite tipove informacija kao što su
- jezik
- slike
- audio
- video
- kod

[Google Cloud Dokumentacija za `Generative Language API` za Python](https://ai.google.dev/api/python/google/generativeai)

Za korištenje ovog <shortcut>API-ja</shortcut> u Python okruženju, bilo je potrebno instalirati `google-generativeai` paket:

```Shell
pip install google-generativeai
```

U dokumentaciji za `Generative Language API`, navedeni su primjeri kako koristiti `genai.GenerativeModel` za pristup <shortcut>API-ju</shortcut>. Korištenjem ovog modela, mogu se generirati sadržaji na osnovu unesenih podataka.

<tabs group="os">
    <tab id="windows-install" title="primjer Python file" group-key="windows">
        <code-block lang="python">
        <![CDATA[
            import google.generativeai as genai
            import os

            genai.configure(api_key=os.environ['API_KEY'])
            
            model = genai.GenerativeModel(name='gemini-1.5-flash')
            response = model.generate_content('Please summarise this document: ...')
            
            print(response.text)
        ]]>
        </code-block>
    </tab>
    <tab id="macos-install" title=".env file" group-key="macos">
        <code-block lang="shell">
        <![CDATA[
            API_KEY=api_kljuc
        ]]>
        </code-block>
    </tab>
</tabs>

> Pod `CREDENTIALS` na `Google Cloud` Platformi se može pronaći `API_KEY` koji se koristi za autentifikaciju prilikom korištenja `Generative Language API`.

`Razlike u verzijama paketa nakon instalacije`:
<compare>
    <code-block lang="shell" collapsible="true" collapsed-title="Person.kt">
        Package            Version
        ------------------ --------
        asgiref            3.8.1
        certifi            2024.2.2
        cffi               1.16.0
        charset-normalizer 3.3.2
        cryptography       42.0.7
        Django             5.0.6
        django-allauth     0.63.2
        idna               3.7
        oauthlib           3.2.2
        pip                24.0
        pycparser          2.22
        PyJWT              2.8.0
        python-dotenv      1.0.1
        requests           2.32.3
        requests-oauthlib  2.0.0
        sqlparse           0.5.0
        stripe             9.9.0
        typing_extensions  4.12.0
        tzdata             2024.1
        urllib3            2.2.1
    </code-block>
    <code-block lang="shell" collapsible="true" collapsed-title="Person.kt">
        Package                      Version
        ---------------------------- --------
        annotated-types              0.7.0
        asgiref                      3.8.1
        cachetools                   5.3.3
        certifi                      2024.2.2
        cffi                         1.16.0
        charset-normalizer           3.3.2
        colorama                     0.4.6
        cryptography                 42.0.7
        Django                       5.0.6
        django-allauth               0.63.2
        google-ai-generativelanguage 0.6.4
        google-api-core              2.19.0
        google-api-python-client     2.131.0
        google-auth                  2.29.0
        google-auth-httplib2         0.2.0
        google-generativeai          0.6.0
        googleapis-common-protos     1.63.1
        grpcio                       1.64.1
        grpcio-status                1.62.2
        httplib2                     0.22.0
        idna                         3.7
        oauthlib                     3.2.2
        pip                          24.0
        proto-plus                   1.23.0
        protobuf                     4.25.3
        pyasn1                       0.6.0
        pyasn1_modules               0.4.0
        pycparser                    2.22
        pydantic                     2.7.3
        pydantic_core                2.18.4
        PyJWT                        2.8.0
        pyparsing                    3.1.2
        python-dotenv                1.0.1
        requests                     2.32.3
        requests-oauthlib            2.0.0
        rsa                          4.9
        sqlparse                     0.5.0
        stripe                       9.9.0
        tqdm                         4.66.4
        typing_extensions            4.12.0
        tzdata                       2024.1
        uritemplate                  4.1.1
        urllib3                      2.2.1
    </code-block>
</compare>

Primjer koda prikazuje kako se koristi `genai.GenerativeModel` za generiranje sadržaja na osnovu unesenih podataka. U ovom slučaju, generira objašnjenje teorije grupa na osnovu unesenog prompta.

<code-block lang="python">
<![CDATA[
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['GENAI_API_KEY'])

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

response = model.generate_content('Objasni sta je teorija grupa.')

print(response.text)
]]>

</code-block>

Output:

<tabs>
<tab title="Konzolni Output">
<code-block>
<![CDATA[

## Teorija grupa: Uvod u svijet simetrije

Teorija grupa je grana matematike koja se bavi proučavanjem **grupa**, a grupa je matematički objekt koji se sastoji od skupa elemenata i operacije koja se nad tim elementima može izvršiti.

Da bismo razumjeli što je grupa, zamislimo **simetrije** nekog objekta. Na primjer, kvadrat ima četiri simetrije:

* **Rotacija za 90 stepeni** oko centra
* **Rotacija za 180 stepeni** oko centra
* **Rotacija za 270 stepeni** oko centra
* **Refleksija** preko horizontale ili vertikale

Sada, zamislite da te simetrije nazovemo **elementima grupe**. Kada izvršimo jednu simetriju, a zatim drugu, dobijemo **novu** simetriju. Na primjer, ako kvadrat rotiramo za 90 stepeni, a zatim ga reflektiramo preko horizontale, dobijemo novu simetriju (rotaciju za 270 stepeni).

Ovaj proces kombinovanja simetrija (elemenata grupe) zove se **operacija grupe**.

**Ključne osobine grupe:**

* **Asocijativnost:** (a * b) * c = a * (b * c) (rezultat je isti bez obzira kako grupišemo elemente)
* **Neutralni element:** postoji element *e* u grupi koji ne mijenja rezultat kada se kombinira s drugim elementima (e * a = a * e = a)
* **Inverzni element:** za svaki element *a* u grupi postoji inverzni element *a⁻¹* koji poništava djelovanje *a* (a * a⁻¹ = a⁻¹ * a = e)

**Primjeri grupa:**

* **Grupa svih rotacija** pravilnog poligona
* **Grupa svih permutacija** skupa elemenata
* **Grupa svih simetrija** nekog geometrijskog tijela
* **Grupa svih cjelobrojnih brojeva** s operacijom sabiranja

**Značaj teorije grupa:**

Teorija grupa ima široku primjenu u raznim granama matematike, fizike, hemije, informatike i drugih disciplina. Koristi se za:

* Analiziranje struktura i simetrija
* Razumijevanje i opisivanje kretanja
* Proučavanje kodova i šifriranja
* Razvijanje modela u fizici čestica
* Razumijevanje kristalnih struktura u hemiji

**Teorija grupa predstavlja moćan alat koji nam pomaže da razumijemo i organizujemo složene koncepte, a ona je i dalje u razvoju i otkrivanju novih primjena.**

    ]]>
</code-block>
</tab>
<tab title="Markdown Output">
## Teorija grupa: Uvod u svijet simetrije

Teorija grupa je grana matematike koja se bavi proučavanjem **grupa**, a grupa je matematički objekt koji se sastoji od skupa elemenata i operacije koja se nad tim elementima može izvršiti.

Da bismo razumjeli što je grupa, zamislimo **simetrije** nekog objekta. Na primjer, kvadrat ima četiri simetrije:

* **Rotacija za 90 stepeni** oko centra
* **Rotacija za 180 stepeni** oko centra
* **Rotacija za 270 stepeni** oko centra
* **Refleksija** preko horizontale ili vertikale

Sada, zamislite da te simetrije nazovemo **elementima grupe**. Kada izvršimo jednu simetriju, a zatim drugu, dobijemo **novu** simetriju. Na primjer, ako kvadrat rotiramo za 90 stepeni, a zatim ga reflektiramo preko horizontale, dobijemo novu simetriju (rotaciju za 270 stepeni).

Ovaj proces kombinovanja simetrija (elemenata grupe) zove se **operacija grupe**.

**Ključne osobine grupe:**

* **Asocijativnost:** (a * b) * c = a * (b * c) (rezultat je isti bez obzira kako grupišemo elemente)
* **Neutralni element:** postoji element *e* u grupi koji ne mijenja rezultat kada se kombinira s drugim elementima (e * a = a * e = a)
* **Inverzni element:** za svaki element *a* u grupi postoji inverzni element *a⁻¹* koji poništava djelovanje *a* (a * a⁻¹ = a⁻¹ * a = e)

**Primjeri grupa:**

* **Grupa svih rotacija** pravilnog poligona
* **Grupa svih permutacija** skupa elemenata
* **Grupa svih simetrija** nekog geometrijskog tijela
* **Grupa svih cjelobrojnih brojeva** s operacijom sabiranja

**Značaj teorije grupa:**

Teorija grupa ima široku primjenu u raznim granama matematike, fizike, hemije, informatike i drugih disciplina. Koristi se za:

* Analiziranje struktura i simetrija
* Razumijevanje i opisivanje kretanja
* Proučavanje kodova i šifriranja
* Razvijanje modela u fizici čestica
* Razumijevanje kristalnih struktura u hemiji

**Teorija grupa predstavlja moćan alat koji nam pomaže da razumijemo i organizujemo složene koncepte, a ona je i dalje u razvoju i otkrivanju novih primjena.**
</tab>
</tabs>
