# 5. Analiza Targeta

## Identifikacija Stakeholdera i Njihovih Zahtjeva

**Ime: ForgeAI**

**Tema: Razvoj VST plugina za generiranje MIDI datoteka putem OpenAI API-ja**

**Opis poslovnog slučaja:**

| **Redni broj** | **Korisnik**               | **Zahtjev**                                                                                                                                                                                                                                          |
|----------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1.**         | **Developeri VST plugina** | Odgovorni za razvoj VST plugina, implementaciju komunikacije s OpenAI API-jem, obradu JSON odgovora i generiranje MIDI datoteka. Njihova odgovornost je osigurati funkcionalnost plugina i njegovu kvalitetu.                                        |
| **2.**         | **Korisnici VST plugina**  | Muzičari i producenti koji koriste digitalne audio radne stanice (DAW) za stvaranje muzike. Oni će koristiti ovaj plugin kako bi generirali MIDI datoteke iz korisničkih upita i integrirali ih izravno u svoje muzičke projekte.                    |
| **3.**         | **OpenAI**                 | Pruža API koji omogućuje korisnicima pristup naprednim umjetničkim inteligencijama (AI). Kroz ovaj API, korisnici mogu poslati upit (prompt) i dobiti odgovor u obliku JSON datoteke koja opisuje MIDI datoteku.                                     |
| **4.**         | **Administratori računa**  | Odgovorni za upravljanje korisničkim računima i pretplatama. Njihova uloga uključuje upravljanje korisničkim podacima, procesuiranje pretplata i pružanje korisničke podrške.                                                                        |
| **5.**         | **Muzičke kompanije**      | Kompanije koje se bave proizvodnjom muzike mogu biti zainteresirane za ovaj plugin kako bi olakšale proces stvaranja muzike svojim zaposlenicima. One bi mogle razmotriti nabavku pretplata za svoje timove ili pružiti plugin kao dio svoje opreme. |

## Analiza Potreba Stakeholdera

1. **Developeri VST plugina:**
    - **Potrebna rješenja:**
        - Stabilna i efikasna implementacija plugina.
        - Integracija s OpenAI API-jem.
        - Efikasna obrada i konverzija JSON odgovora u MIDI format.
    - **Ciljevi:**
        - Osigurati visoku funkcionalnost i kvalitetu plugina.
        - Kontinuirano održavanje i unapređenje softvera.

2. **Korisnici VST plugina:**
    - **Potrebna rješenja:**
        - Intuitivan i jednostavan za korištenje plugin.
        - Brza i precizna generacija MIDI datoteka iz korisničkih upita.
    - **Ciljevi:**
        - Povećanje kreativnosti i efikasnosti u stvaranju muzike.
        - Integracija generiranih MIDI datoteka u muzičke projekte bez problema.

3. **OpenAI:**
    - **Potrebna rješenja:**
        - Stabilna i sigurna veza s korisnicima putem API-ja.
        - Precizno i pouzdano generiranje odgovora u JSON formatu.
    - **Ciljevi:**
        - Osigurati visoku dostupnost i pouzdanost API-ja.
        - Zadovoljstvo korisnika s kvalitetom generiranih podataka.

4. **Administratori računa:**
    - **Potrebna rješenja:**
        - Efikasno upravljanje korisničkim podacima i pretplatama.
        - Pravovremena podrška korisnicima.
    - **Ciljevi:**
        - Osigurati korisničko zadovoljstvo i lojalnost.
        - Optimalno upravljanje resursima i korisničkim računima.

5. **Muzičke kompanije:**
    - **Potrebna rješenja:**
        - Pristup VST pluginu za njihove timove.
        - Efikasno korištenje plugina u proizvodnji muzike.
    - **Ciljevi:**
        - Povećanje produktivnosti i kreativnosti zaposlenika.
        - Inovacije u procesu stvaranja muzike.