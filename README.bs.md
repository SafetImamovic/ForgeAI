<a href="https://github.com/SafetImamovic/ForgeAI/blob/main/README.md"><img src="https://img.shields.io/badge/Lang-EN-red" alt="Lang EN" height="23"></a> <a href="https://github.com/SafetImamovic/ForgeAI/blob/main/README.bs.md"><img src="https://img.shields.io/badge/Lang-BS-blue" alt="Lang BS" height="24"></a>
<a href="https://safetimamovic.github.io/"><img src="https://img.shields.io/badge/Projektna%20Dokumentacija-black" alt="Projektna Dokumentacija" height="28"></a>

# ForgeAI

**ForgeAI** je VST dodatak (trenutno prototip kao web stranica) dizajniran za generiranje **[MIDI](https://en.wikipedia.org/wiki/MIDI)** datoteka na temelju tekstualnih podataka koje korisnik unese.

Koristi napredne AI modele za pretvaranje tekstualnih opisa u MIDI format, čime proces kreiranja muzike postaje intuitivniji i efikasniji.

## Tehnički Opis

### Arhitektura

- **Korisničko Sučelje**: Intuitivno sučelje za unos tekstualnih upita.
- **Autentifikacija**: Siguran sustav autentifikacije i upravljanja pretplatama.
- **Backend Server**: Obradjuje korisničke upite, komunicira s **Google Gemini** i upravlja podacima.
- **Google Gemini**: Vanjski API za generiranje muzike na temelju tekstualnih opisa.
- **Algoritam Konverzije**: Pretvara JSON odgovore iz **Google Gemini** API-ja u MIDI format.

### Proces Generiranja MIDI Datoteke

- **Korisnički Unos**: Korisnik unosi tekstualni upit u sučelje dodatka.
- **Autentifikacija**: Provjerava pretplatu korisnika.
- **Obrada na Serveru**: Upit se šalje serveru i proslijeđuje **Google Gemini** API-ju.
- **Generiranje Odgovora**: **Google Gemini** API vraća JSON odgovor na temelju upita.
- **Konverzija u MIDI**: Algoritam pretvara JSON u MIDI datoteku.
- **Preuzimanje Datoteke**: Korisnik preuzima MIDI datoteku za korištenje u **[DAW](https://en.wikipedia.org/wiki/Digital_audio_workstation)**-u.

### Tehnologije

- **Frontend**: HTML, CSS, JavaScript
- **Backend + Baza Podataka**: Django (Python)
- **Integracija API-ja**: Google Gemini
- **Plaćanje**: Stripe
- **Algoritmi**: Prilagođeni algoritmi za pretvaranje JSON-a u MIDI

## Zaključak

**ForgeAI** predstavlja naprednu tehnologiju u području produkcije muzike, omogućavajući korisnicima intuitivno i efikasno generiranje muzike.

Korištenjem tekstualnih upita i naprednih AI modela, ForgeAI pojednostavljuje proces stvaranja muzike, pružajući visoku kvalitetu i fleksibilnost.

Ovaj projekt ima potencijal da značajno unaprijedi način na koji profesionalci iz svijeta muzike i ljubitelji stvaraju muziku, čineći ga pristupačnijim i efikasnijim.