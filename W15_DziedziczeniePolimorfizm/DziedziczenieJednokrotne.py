class A:
    def info(self):
        print("Klasa A")
        
class B(A):
    def info(self):
        print("Klasa B")
        
class C(B):
    def info(self):
        print("Klasa C")
        
print("Tworzymy obiekt i sprawdzamy czyja metoda sie wywola:")
obiekt = C()
obiekt.info()
print("Kolejnosc wywolywania metod z klas:")
print(C.__mro__)
print(C.mro())