class Korisnik():
    def __init__(self):
        self.id = 0;
        self.ime = "ime";
        self.prezime = "prezime";
    
    def __init__(self, id, ime, prezime):
        self.id = id;
        self.ime = ime;
        self.prezime = prezime;
        
    def getIme(self):
        return self.ime;