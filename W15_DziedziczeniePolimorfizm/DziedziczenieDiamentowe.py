class A:
    def info(self):
        print("Klasa A")
        
class B(A):
    def info(self):
        print("Klasa B")
        
class C(A):
    def info(self):
        print("Klasa C")

class D(B,C):
    pass
    
print("Tworzymy obiekt i sprawdzamy czyja metoda sie wywola:")
obiekt = D()
obiekt.info()
print("Kolejnosc wywolywania metod z klas:")
print(D.__mro__)
print(D.mro())