def pomnozLiczby2(liczba1, liczba2):
    return liczba1*liczba2

def pomnozLiczby(*liczby):
    wynik = 1
    for liczba in liczby:
        print(liczba)
        wynik*=liczba
    return wynik    
    
print("Zwykle mnozenie: ",pomnozLiczby2(2,4))
print("Mnozenie 3 liczb: ",pomnozLiczby(1,2,3))
print("Mnozenie 5 liczb: ",pomnozLiczby(1,2,3,4,5))
