class Osoba:
    def __init__(dane):
        im = input("Podaj imie: ")
        naz = input ("Podaj nazwisko: ")
        tel = input ("Wpisz numer telefonu: ")
        dane.imie = im
        dane.nazwisko = naz
        dane.telefon = tel
    
    def __str__(self):
        return f"Imie: {self.imie}, nazwisko: {self.nazwisko}, tel.:{self.telefon}."
    
    def info(self):
        print("Imie: ",self.imie)
        print("Nazwisko: ",self.nazwisko)
        print("Telefon: ",self.telefon)

class Pusta:
    pass


jan = Osoba()
ala = Pusta()
print("To jest to co zwroci klasa Osoba")
print(jan)
print("To jest to co zwroci klasa Pusta")
print(ala)
print("A to jest wywolanie funkcji info na Osobie")
jan.info()