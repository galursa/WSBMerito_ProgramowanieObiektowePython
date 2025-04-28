# -*- coding: utf-8 -*-
krotka=(1,2,6,2,8,1)
krotka2 = (5,3,1,9)
krotka3=krotka+krotka2
print("To jest polaczona krotka:",krotka3)
krotka3=krotka2*3
print("A to jest potrojona krotka:",krotka3)
print("Można w ten sposob rozpakowac krotke:")
(a,b,c,d)=krotka2
print("Zmienna a:",a)
print("Zmienna b:",b)
print("Zmienna c:",c)
print("Zmienna d:",d)
print("Policzymy teraz ile jedynek jest w polaczonej krotce")
print(krotka3.count(1))