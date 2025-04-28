# -*- coding: utf-8 -*-
lista = ["white","red", "blue"]
lista[1:1] = ["yellow","green"]
print("Lista rozszerzona: ",lista)
lista.insert(2,"ochre")
print("Lista po dodaniu elementu na pozycji 2 ",lista)
lista.append("pink")
print("Lista po zastosowaniu komendy append: ",lista)
niebieskie=["azure", "indygo"]
lista.extend(niebieskie)
print("Rozszerzona lista o kolory niebieski: ",lista)
lista.remove("green")
print("Usuwamy green z listy: ",lista)
lista.pop(4)
print("Usuwamy z listy element na pozycji 4:",lista)
lista.pop()
print("Usuwamy ostatni element z listy:",lista)
del lista[1]
print("Usuwamy z listy element na pozycji 1:",lista)
del lista
print("Usunelismy cala liste.")