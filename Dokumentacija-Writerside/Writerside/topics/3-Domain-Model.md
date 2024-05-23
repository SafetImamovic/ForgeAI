# 3. Domain Model

<code-block lang="plantuml" max-width="10px">
<![CDATA[
@startuml

scale 640 width

object Korisnik {
    id = 123
    ime = "John Doe"
    email = "john@example.com"
    pretplataAktivna = true
}

object Pretplata {
    id = 456
    korisnikId = 123
    datumPocetka = "2024-01-01"
    datumZavrsetka = "2024-12-31"
}

object Prompt {
    id = 789
    korisnikId = 123
    tekst = "Generate a calm piano melody."
}

object OpenAIResponse {
    jsonOdgovor = { "notes": ["C", "E", "G"], "duration": 4 }
}

object MIDIFile {
    jsonPodaci = { "notes": ["C", "E", "G"], "duration": 4 }
}

@enduml
]]>
</code-block>