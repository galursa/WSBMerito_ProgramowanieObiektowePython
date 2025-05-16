
# Klasa Produkt
class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc 

    def info(self):
        print("Produkt: ",self.nazwa)
        print("Cena: ",self.cena," zl")
        print("Ilosc: ",self. ilosc)
    
    def cenaZaSztuke(self):
        return self.cena/self.ilosc        
        
# Klasa bazowa Magazyn
class Magazyn:
    def __init__(self, produktyNaStanie):
        self.produktyNaStanie = []

    def dodajDoMagazynu(self, produkt):
        self.produktyNaStanie.append(produkt)
    
    def wyswietlZawartosc(self):
        for produkt in self.produktyNaStanie:
            print("Nazwa: ",produkt.nazwa)
            print("Cena: ",produkt.cena)
            print("Ilosc: ",produkt.ilosc)              

# Klasa potomna Sklep dziedziczy po klasie Magazyn
class Sklep(Magazyn):
    def __init__(self, nazwa, adres):
        super().__init__(self)
        self.nazwa = nazwa
        self.adres = adres

    def wyswietlDaneAdresowe(self):
        print("***********")
        print(self.nazwa)
        print("***********")
        print(self.adres)
    
    def wpiszDane(self):
        decyzja = "t"
        while(decyzja == "t"):
            nazwa = input("Podaj nazwe produktu: ")
            cena = input("Podaj cene produktu w zlotych: ")
            ilosc = input("Podaj ilosc proudktu na magazynie: ")
            produkt = Produkt(nazwa,cena,ilosc)
            self.dodajDoMagazynu(produkt)
            decyzja = input("Czy chcesz dodac nastepny produkt - t ?")
            
        
stonka = Sklep("Stonka", "Ziemniaczana 13, 13-130 Ogrodowo")
stonka.wyswietlDaneAdresowe()
stonka.wpiszDane()
stonka.wyswietlZawartosc()