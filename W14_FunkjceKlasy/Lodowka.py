class Lodowka:
    def __init__(self):
        self.produkt=[]
    
    def dodajProdukt(self, nazwa, terminPrzydatnosci, ilosc):
        self.produkt.append((nazwa, terminPrzydatnosci, ilosc))   
        
    def wyswietlProdukty(self):
        print("---------------------")
        print("Lodowka - zawartosc: ")
        print("---------------------")
        for produkt in self.produkt:
            print(produkt)
        print()
        
    def znajdzProdukt(self,nazwa):
        for element in self.produkt:
            if element[0]==nazwa:
                print("Znaleziono")
                print(element)
                break
        else:
            print("Nie znaleziono produktu")
        print()
        
    def usunProdukt(self, nazwa):
        for element in self.produkt:
            if element[0]==nazwa:
                self.produkt.remove(element)
                print("Usunieto")
                break
        else:
            print("Szukanego produktu nie ma w lodwoce")
        print()
            
duzaLodowka = Lodowka()
duzaLodowka.dodajProdukt("jajko", "1.07.2025", 20)
duzaLodowka.dodajProdukt("Maslo", "15.06.2025", 5)
duzaLodowka.dodajProdukt("Mleko", "20.06.2025", 2)
duzaLodowka.wyswietlProdukty()
duzaLodowka.znajdzProdukt("jajko")
duzaLodowka.znajdzProdukt("kielbasa")
duzaLodowka.usunProdukt("jajko")
duzaLodowka.usunProdukt("kielbasa")
duzaLodowka.wyswietlProdukty()
