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
slownik.update({"orange": "pomaranczowy"})
print("Slownik po dodaniu elementu:",slownik)
slownik.popitem()
print("Usunelismy element i slownik to: ",slownik)
del slownik["cmyk"]
print("Usunelismy element cmyk:",slownik)
slownik.clear()
print("Usunelismy zawartosc slownika: ",slownik)