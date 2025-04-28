# -*- coding: utf-8 -*-
lista = ["white","red", "blue"]
print("Oto lista wyswietlona w petli - odpowiednik petli foreach:")
for x in lista:
    print(x)
    
print("Mozna jeszcze wyswietlic w ten sposob")
for i in range(len(lista)):
  print(i,":",lista[i])

print("W petli while tez sie uda")
i = 0
while i < len(lista):
  print(i,":",lista[i])
  i+=1
  
print("Mozna uzyc tez List Comprehension")
[print(x) for x in lista]