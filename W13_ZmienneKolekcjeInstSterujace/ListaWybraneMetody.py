# -*- coding: utf-8 -*-
lista = ["white","red", "blue", "yellow", "pink","orange","green"]
print("Nasza lista: ",lista)
lista.sort()
print("Listy mozna sortowac:",lista)
lista.sort(reverse=True)
print("Listy mozna tez odwrotnie sortowac:",lista)
listaMniejsza = lista[2:4]
print("Liste mozna skopiowac w kawalku, tu od 2 do 4 pozycji:",listaMniejsza)
listaBlue = ["azure","indygo"]
listaDuza=listaMniejsza+listaBlue
print("Polaczone listy:",listaDuza)
listaDuza.remove("azure")
print("Usuwamy element azure:",listaDuza)
