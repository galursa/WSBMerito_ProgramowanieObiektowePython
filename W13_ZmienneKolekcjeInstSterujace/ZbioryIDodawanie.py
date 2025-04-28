# -*- coding: utf-8 -*-
zbior={"a","c","d","b"}
zbior2={"e","f"}
zbior3=zbior.union(zbior2)
print("Zbior 1:",zbior)
print("Zbior 2:",zbior2)
print("Polaczono zbiory: ",zbior3)
zbior4=zbior3|zbior2
print("Kolejny przyklad laczenia: ",zbior4)
zbior.update(zbior2)
print("Teraz uakutalnilismy zbior 1 dodajac do niego zbior 2:",zbior)
print("Przypomnijmy zbior 1:",zbior)
print("Zbior 2:",zbior2)
print("A ich przeciecie - czesc wspolna: ",zbior.intersection(zbior2))
print("Oraz roznica: ",zbior.difference(zbior2))