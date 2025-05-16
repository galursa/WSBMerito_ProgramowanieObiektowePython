import math

#Klasa Bazowa 1
class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    
    def napiszFunkcje(self):
        print(f"f(x)={self.a}x² +{self.b}x+{self.c}")

#Klasa bazowa 2
class Pierwiastki:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def delta(self):
        return self.b**2 - 4*self.a*self.c
    
    def pierwiastki(self):
        d=self.delta()
        listaPierwiastkow = []
        if d<0:
            del listaPierwiastkow
            return "Delta ujemna brak miejsc zerowych"
        elif d==0:
            x0 = -self.b/(2*self.a)
            listaPierwiastkow.append(x0)
            return listaPierwiastkow
        else:
            x1 = (-self.b -math.sqrt(d))/(2*self.a)
            x2 = (-self.b +math.sqrt(d))/(2*self.a)
            listaPierwiastkow.append(x1)
            listaPierwiastkow.append(x2)
            return listaPierwiastkow
  
#Klasa potomna
class FunkcjeObliczenia(FunkcjaKwadratowa, Pierwiastki):
    def __init__(self,a,b,c):
        FunkcjaKwadratowa.__init__(self,a, b, c)
        Pierwiastki.__init__(self, a, b, c)
    
    def pobierzDane(self):
        self.a = int(input("Podaj a: "))
        self.b = int(input("Podaj b: "))
        self.c = int(input("Podaj c: "))
        
    def wyswietlDelte(self):
        print("Delta = ", Pierwiastki.delta(self))
    
    def wyswietlPierwiastki(self):
        listaPierwiastkow =  Pierwiastki.pierwiastki(self)
        i = 0;
        for pierwiastek in listaPierwiastkow:
            print("x",i," = ",pierwiastek)
            i+=1
        
print("Obiekt klasy FunkcjaKwadratowa")
f1 = FunkcjaKwadratowa(1,2,3)
f1.napiszFunkcje()
print()
print("Obiekt klasy Pierwiastki")
p = Pierwiastki(3,5,1)
print("Delta = ",p.delta())
print("Pierwiastki:")
print(p.pierwiastki())
print()
print("Obiekt klasy FunkcjeObliczenia")
obliczenia = FunkcjeObliczenia(2,6,1)
obliczenia.pobierzDane()
obliczenia.wyswietlDelte()
obliczenia.wyswietlPierwiastki()

