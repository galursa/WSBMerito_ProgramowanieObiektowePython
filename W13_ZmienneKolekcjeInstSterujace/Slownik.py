# -*- coding: utf-8 -*-
slownik ={
    "red": "czerwony",
    "blue": "niebieski",
    "green": "zielony",
    "ilosc": 3,
    "cmyk": ["cyan","magenta","yellow","black"]
    }
print("Slownik:")
print(slownik)
print("A jego dlugosc: ",len(slownik))
print("Wyswietle element na pozycji blue",slownik["blue"])
print("Wysiwetle zawartosc z klucza cmyk:", slownik.get("cmyk"))
slownik["pink"]="rozowy"
print("Slownik po dodaniu elementu:",slownik)
print("Sprawdzmy klucze:",slownik.keys())
print("Sprawdzmy wartosci:",slownik.values())
print("Wyswietlmy klucze i wartosci:",slownik.items())