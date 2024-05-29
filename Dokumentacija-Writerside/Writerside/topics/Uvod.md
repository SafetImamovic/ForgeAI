# 1. Uvod

U današnjem visoko konkurentnom tržištu, uspješno plasiranje proizvoda ili usluga zahtijeva iznimnu organizaciju, efikasnost i sposobnost upravljanja velikim količinama informacija. ForgeAI je inovativan VST plugin dizajniran da generira MIDI datoteke na osnovu korisničkog unosa tekstualnih podataka. Kroz ovaj projekt, ForgeAI nudi jedinstvenu priliku za muzičke profesionalce i entuzijaste da koriste naprednu tehnologiju za stvaranje muzike na intuitivan i efikasan način.

Projekt podrazumijeva korisničku autentifikaciju i pretplatu na mjesečnoj osnovi, omogućavajući korisnicima unos prompta koji se šalje serveru. Server obrađuje unos i koristi OpenAI API za generiranje odgovora u unaprijed definisanom JSON formatu. Na osnovu ovih podataka, klijentski algoritam formira MIDI datoteku koja se može integrirati u Digital Audio Workstation (DAW). Cilj ovog projekta je pružiti korisnicima alat koji pojednostavljuje proces stvaranja muzike, omogućavajući brže i kreativnije rezultate.

# Tehnički Opis

## Opis Sistemske Arhitekture

Sistemska arhitektura ForgeAI-a sastoji se od nekoliko ključnih komponenti:

1. **Korisnički Interfejs (UI):** Intuitivan interfejs koji omogućava korisnicima unos tekstualnih prompta.
2. **Autentifikacija i Pretplata:** Sistem za autentifikaciju korisnika i upravljanje pretplatama, osiguravajući pristup samo ovlaštenim korisnicima.
3. **Server:** Backend server koji prima korisničke unose, komunicira s OpenAI API-jem i upravlja podacima.
4. **OpenAI API:** Eksterni API koji obrađuje korisničke unose i generira JSON odgovor.
5. **Algoritam za Generiranje MIDI Datoteka:** Algoritam koji konvertira JSON podatke u MIDI format, prilagođen za korištenje u DAW-ovima.

## Proces Generiranja MIDI Datoteka

1. **Korisnički Unos:** Korisnik unosi tekstualni prompt kroz UI plugin-a.
2. **Autentifikacija:** Sistem provjerava korisnički status pretplate.
3. **Obrada na Serveru:** Unos se šalje serveru koji prosljeđuje zahtjev OpenAI API-ju.
4. **Generiranje Odgovora:** OpenAI API vraća JSON odgovor baziran na promptu.
5. **Konverzija u MIDI:** JSON odgovor se obrađuje algoritmom koji generira odgovarajući MIDI fajl.
6. **Preuzimanje MIDI Datoteke:** Korisnik preuzima generiranu MIDI datoteku za dalju upotrebu u svom DAW-u.

# Funkcionalnosti i Korisničke Prednosti

## Ključne Funkcionalnosti

- **Tekstualni Prompt:** Korisnici mogu unositi specifične tekstualne zahtjeve koji definiraju karakteristike željene muzike.
- **Autentifikacija i Pretplata:** Siguran sistem autentifikacije i pretplate koji omogućava pristup servisu samo ovlaštenim korisnicima.
- **Integracija s DAW-om:** Generirane MIDI datoteke su kompatibilne s većinom popularnih DAW-ova.

## Prednosti za Korisnike

- **Brza Generacija Muzike:** Automatizirani proces omogućava brzu i efikasnu generaciju muzike, štedeći vrijeme korisnika.
- **Kreativna Fleksibilnost:** Korištenjem tekstualnih prompta, korisnici imaju veliku fleksibilnost u definiranju muzičkih elemenata.
- **Visoka Kvaliteta:** Korištenjem napredne AI tehnologije, generirane MIDI datoteke su visoke kvalitete i prilagođene profesionalnim standardima.

# Tehnički Detalji

## Tehnologije i Alati

- **Frontend:** HTML, CSS, JavaScript za izgradnju korisničkog interfejsa.
- **Backend:** Django za server-side logiku i middleware sesije.
- **API Integracija:** OpenAI API za generiranje muzike na osnovu tekstualnih unosa.
- **Baza Podataka:** Supabase za pohranu korisničkih podataka i autentifikaciju.
- **Plaćanje:** Stripe za upravljanje plaćanjima i pretplatama.
- **Algoritmi:** Custom algoritmi za konverziju JSON podataka u MIDI format.

# Zaključak

ForgeAI predstavlja naprednu tehnologiju u svijetu muzičke produkcije, omogućavajući korisnicima intuitivno i efikasno generiranje muzike. Korištenjem tekstualnih prompta i naprednih AI modela, ForgeAI olakšava proces stvaranja muzike, pružajući visoku kvalitetu i fleksibilnost. Ovaj projekt ima potencijal značajno unaprijediti način na koji muzički profesionalci i entuzijasti kreiraju muziku, čineći je pristupačnijom i efikasnijom.