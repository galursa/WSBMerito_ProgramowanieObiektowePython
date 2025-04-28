import random
liczba1 = random.randrange(1,10)
liczba2 = random.randrange(5,15)
print("Liczba1=",liczba1)
print("Liczba1=",liczba2)
if liczba1 > liczba2:
    print(liczba1, " jest wieksza do od, ",liczba2)
elif liczba1 == liczba2:
    print(liczba1, "jest rowna: ",liczba2)
else:
    print(liczba2, "jest wieksza od ", liczba1)    
    