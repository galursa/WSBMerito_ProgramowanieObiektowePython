class Farby:
    def __init__(self,nazwa,cena,producent):
        self.nazwa = nazwa
        self.cena = cena
        self.producent = producent
    
    def wyswietlInfo(self):
        print("Nazwa:", self.nazwa)
        print("Cena: ", self.cena)
        print("Producent", self.producent)
        
akwarele = Farby("Wodne", 22.99, "Wodne Szalenstwo")
akwarele.wyswietlInfo()
        
    