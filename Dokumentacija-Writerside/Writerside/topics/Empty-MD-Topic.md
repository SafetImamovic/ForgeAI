# Specifikacija funkcionalnih i nefunkcionalnih zahtjeva

## Korisnik | AI MIDI Generator

| **Redni broj** | **Zahtjev**                           | **Opis**                                                                         |
|----------------|---------------------------------------|----------------------------------------------------------------------------------|
| F1             | Registracija                          | Sistem treba da obezbijedi registraciju novog korisnika koji mu pristupa.        |
| F2             | Logovanje                             | Sistem treba da obezbijedi autentifikaciju korisnika koji mu pristupa.           |
| F3             | Omogučavanje tekstualnog prompt unosa | Sistem treba da obezbijedi tekstualni prompt unos preko terminala/GUI            |
| F4             | Generisanje MIDI fajlova              | Sistem će omogućiti muzičaru generisanje MIDI fajlova korištenjem AI algoritama. |
| F5             | Preuzimanje MIDI fajlova              | Sistem će omogućiti muzičaru preuzimanje kreiranih MIDI fajlova na svoj uređaj.  |
| F6             | Pregled generisanih fajlova           | Sistem će omogućiti muzičaru pregled generisanih fajlova unutar aplikacije.      |

## Korisnik | Stranica

| **Redni broj** | **Zahtjev**               | **Opis**                                                                                                                        |
|----------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| F1             | Registracija              | Korisnici se mogu registrirati na stranici kako bi pristupili dodatnim funkcijama i uslugama.                                   |
| F2             | Logovanje                 | Omogućuje korisnicima prijavu na svoje račune koristeći svoje vjerodajnice.                                                     |
| F3             | Pregled računa            | Korisnici mogu pregledati informacije o svom računu, kao što su pretplate, povijest transakcija i druge relevantne informacije. |
| F4             | Odabir načina plaćanja    | Korisnici mogu odabrati željeni način plaćanja prilikom kupovine pretplate ili proizvoda/usluga.                                |
| F5             | Preuzimanje VST Plugina   | Korisnici mogu preuzeti VST plugin s web stranice kako bi ga integrirali u svoje digitalne audio radne stanice.                 |
| F6             | Ukidanje pretplate        | Pruža korisnicima mogućnost da otkažu pretplatu i prestanu s korištenjem dodatnih usluga.                                       |
| F7             | Brisanje računa           | Omogućuje korisnicima brisanje svog korisničkog računa i povezanih podataka iz sustava.                                         |

## Nefunkcionalni Zahtjevi

| **Redni broj** | **Zahtjev**                    | **Opis**                                                                                                                                                                                     |
|----------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| N1             | Sigurnost                      | Podacima u sistemu neće moći da pristupaju svi korisnici. Pristup će biti ograničen na osnovu uloga korisnika. Autentifikacija i autorizacija će biti implementirani za osiguranje podataka. |
| N2             | Performanse                    | Sistem mora omogućiti brzu i efikasnu generaciju i obradu MIDI fajlova. Latencija prilikom korisničkih akcija mora biti minimalna.                                                           |
| N3             | Integritet podataka            | Sistem će imati mehanizme za provjeru i validaciju podataka kako bi se spriječili neispravni unosi i gubitak podataka.                                                                       |
| N4             | Implementacija i pristupačnost | Sistem će biti implementiran kao cloud aplikacija dostupna korisnicima sa različitih uređaja. Nema potrebe za specijalizovanim hardverom ili instalacijom softvera na korisničkim uređajima. |
| N5             | Skalabilnost                   | Sistem mora biti sposoban da se skaluje u zavisnosti od broja korisnika i obima podataka bez gubitka performansi.                                                                            |
| N6             | Uslužnost                      | Korisnička podrška će biti dostupna za pomoć korisnicima prilikom korištenja sistema. Dokumentacija i tutorijali će biti obezbijeđeni za lakše snalaženje.                                   |
| N7             | Usaglašenost                   | Sistem će biti usaglašen sa relevantnim pravnim i industrijskim standardima za zaštitu podataka i digitalna prava.                                                                           |
| N8             | Fleksibilnost                  | Sistem će omogućiti korisnicima prilagođavanje generisanih MIDI fajlova prema njihovim specifičnim potrebama i preferencijama.                                                               |