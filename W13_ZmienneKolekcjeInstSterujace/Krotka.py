# -*- coding: utf-8 -*-
krotka=(1,2,6,2,8,1)
print("To jest krotka: ",krotka)
krotka1 = (1,2,("ala","ola"),4,5)
print("To tez jest krotka: ",krotka1)
print("A to trzeci element pierwszej krotki",krotka[2])
print("A to kawalek pierwszej krotki:",krotka[2:5])
print("A jak chcemy dodać element to mamy dwie mozliwosci")
print("Zamieniamy krotke na liste i dodajemy element")
print("a potem zaminiamy liste na krotke")
lista = list(krotka)
lista.append(9)
krotka = tuple(lista)
print("To jest lista:",lista)
print("A to jest krotka po dodaniu elementu: ",krotka)
print()
print("Mozna tez dodac krotke do krotki")
element = (3,)
krotka+=element
print("Po dodaniu: ",krotka)
