# -*- coding: utf-8 -*-
zbior={"a","c","d","b"}
print("Oto zbior:",zbior)
print("Dlugosc zbioru:",len(zbior))
lista=["e","f"]
zbiorZListy=set(lista)
print("To jest lista: ",lista)
print("A to jest zbior z listy: ",zbiorZListy)
zbior.discard("a")
print("Usunieto a ze zbioru:, ta metoda nie zwraca bledu gdy brak elementu",zbior)
zbior.pop()
print("Ta metoda usuwa element ze zbioru:",zbior)
print("Proba usuniecia nieistniejacego elemntu, metoda ktora zwroci blad")
zbior.remove("g")


