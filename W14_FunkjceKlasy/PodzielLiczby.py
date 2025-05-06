def podzielLiczby(liczba1, liczba2=1):
    if liczba2==0:
        print("Dzielenie przez zero")
        return 0
    return liczba1/liczba2

def funkcjaPusta():
    pass
    
print("Zwykle mnozenie: ",podzielLiczby(2))
print("Zwykle mnozenie: ",podzielLiczby(6,2))   
print("Ponizej bedzie wywolanie pustej funkcji")
funkcjaPusta()
print("Po wywolaniu funkcji pustej")
