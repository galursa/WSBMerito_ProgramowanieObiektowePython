import random
liczba1 = random.randrange(1,10)
print("Czy Liczba1=",liczba1,"zawiera sie w przedziale od 2 do 5?")
if liczba1 >= 2 and liczba1 <= 5:
    print("Tak, podana liczba zawiera sie w przedziale.")
else:
    print("Nie, podana liczba nie zawiera sie w przedziale.")

print("Czy Liczba1=",liczba1,"nie zawiera sie w przedziale od 2 do 5?")
if liczba1 < 2 or liczba1 > 5:
    print("Nie zawiera sie w przedziale")
else:
    print("Zawiera sie przedziale")
if not (liczba1 >= 2 and liczba1 <= 5):        
    print("Nie zawiera sie w przedziale")
else:
    print("Zawiera sie przedziale")        
#jak chcemy miec pustego ifa to musimy dac slowo kluczowe pass
if liczba1 <100:
    pass