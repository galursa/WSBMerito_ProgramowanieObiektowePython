przyslowie = """Siala baba mak,
Nie wiedziala jak,
A dziad wiedzial
nie powiedzial
A to bylo tak
"""
print(przyslowie)
#wyswietla dlugosc lancucha znakow
print(len(przyslowie))
#wyswietla pierwszy znak
print("Pierwsza litera ",przyslowie[0])
#sprawdza czy slowo jest w lancuchu znakow
print("baba" in przyslowie)
#sprawdza czy slowo nie jest w lancuchu znakow
print("dziad" not in przyslowie)
#wyswietla lancuch znakow od poczatku do pozycji 15
print(przyslowie[:15])
#wyswietla lancuch znakow od pozycji 6 do pozycji 15
print(przyslowie[6:15])
#wyswietla lancuch znakow od od pozycji 15 do konca
print(przyslowie[15:])
#wyswietla lancuch znakow od 10 znakow od konca (wstecz) do 3 znakow od konca (wstecz)
print(przyslowie[-10:-3])
print()
komunikat = "Liczba zespolona"
#deklaracja liczb zespolonych
z1=3+5j
z2=1+1j
#laczymy dwie zmienne w jednym komunikacie
print(komunikat,z1)
#dodajemy zmienne zespolone do siebie
print(z1+z2)

