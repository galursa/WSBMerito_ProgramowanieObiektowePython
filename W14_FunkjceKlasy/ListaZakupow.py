class ListaZakupow:
    def __init__(self):
        self.listaZakupow = {}
        
    def dodajProdukt(self):
        produkt = input("Wpisz produkt: ")
        ilosc = input("Wpisz ilosc: ")
        self.listaZakupow[produkt]=ilosc
    
    def usunProdukt(self,produkt):
        self.listaZakupow.pop(produkt)
    
    def wyswietlListe(self):
        i = 1
        for zakup in self.listaZakupow:
            tekst = f"{i} . {zakup} w ilosci {self.listaZakupow[zakup]} sztuk  "
            print(tekst)
            i+=1
        

spozywcze = ListaZakupow()
koniec = "n"
while(koniec!="t"):
    spozywcze.dodajProdukt()
    koniec = input("Czy chcesz zakonczyc = t - tak, n - nie: ")
    
spozywcze.wyswietlListe()
usun = input("Podaj produkt do usuniecia ")
spozywcze.usunProdukt(usun)
spozywcze.wyswietlListe()
