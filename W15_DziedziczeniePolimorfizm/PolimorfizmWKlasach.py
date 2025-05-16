import math 

class Funkcje:
    def oblicz(self, x):
        return x
    
    def wyswietlPostac(self):
        print(" ")
        
    def wyswietlTabele(self, listaX):
        for x in listaX:
            print(x," | ",self.oblicz(x))


# Funkcja liniowa: f(x) = ax + b           
class FunkcjaLiniowa(Funkcje):
    def __init__(self, a, b):
        self.a = a
        self.b = b 
        
    def oblicz(self,x):
        return self.a*x + self.b
    
    def wyswietlPostac(self):
        print(f"f(x)={self.a}x+{self.b}")

# Funkcja wykładnicza: f(x) = a * e^(bx)  
class FunkcjaWykladnicza(Funkcje):
    def __init__(self, a, b):
        self.a = a
        self.b = b 
    
    def oblicz(self,x):
        return self.a * math.exp(self.b*x)
    
    def wyswietlPostac(self):
        print(f"f(x)={self.a}e^({self.b}x)")
        
listaX=[-2, -1, 0, 1, 2]

fLiniowa = FunkcjaLiniowa(2, 1)
fWykladnicza = FunkcjaWykladnicza(1 ,1)
print("Funkcja Liniowa postaci")
fLiniowa.wyswietlPostac()
print("Tabelka wartosci:")
fLiniowa.wyswietlTabele(listaX)
print("Funkcja wykladnicza postaci ")
fWykladnicza.wyswietlPostac()
print("Tabelka wartosci:")
fWykladnicza.wyswietlTabele(listaX)
