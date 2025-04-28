# -*- coding: utf-8 -*-
slownik ={
    "red": "czerwony",
    "blue": "niebieski",
    "green": "zielony",
    "ilosc": 3,
    "cmyk": ["cyan","magenta","yellow","black"]
    }
print("Wyswietla elementy")
for element in slownik:
    print(element)
    
print("Wyswietla klucze")
for klucz in slownik.keys():
    print(klucz)
    
print("Wyswietla wartosci")
for wartosci in slownik.values():
    print(wartosci)
    
print("Wyswietla klucz i wartosc")
for klucz,wartosc in slownik.items():
    print(klucz," : ",wartosc)
    
    