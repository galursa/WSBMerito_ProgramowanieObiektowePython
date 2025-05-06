class LamiglowkiSlowne:
    def __init__(self):
        self.slowa=[]
        
    def podajSlowa(self,ile):
        for i in range(1,ile+1):
            slowo = input("Wpisz slowo:")
            self.slowa.append(slowo)

    def wyswietlSlowa(self):
        ilosc = len(self.slowa)
        for i in range(0,ilosc):
            print(self.slowa[i])
    
    def czyAnagramy(self,slowo1,slowo2):
        litery1 = list(slowo1)
        litery2 = list(slowo2)
        dlugosc1 = len(litery1)
        dlugosc2 = len(litery2)
        if dlugosc1 == dlugosc2:
            litery1.sort()
            litery2.sort()
            for i in range(0,dlugosc1):
                if(litery1[i]!=litery2[i]):
                    return False
        else:
            return False
        return True
        


lamiglowki = LamiglowkiSlowne()          
lamiglowki.podajSlowa(3)
lamiglowki.wyswietlSlowa()
print("Porownuje dwa slowa rozne: ")
print(lamiglowki.czyAnagramy("ala", "kot"))
print("Porownuje dwa slowa takie same:")
print(lamiglowki.czyAnagramy("Kot", "Kot"))   