import random
miesiac = random.randrange(1,13)
match miesiac:
    case 1:
        print("Styczen")
    case 2:
        print("luty")
    case 3: 
        print("Marzec")
    case 4: 
        print("Kwiecien")
    case 5: 
        print("Maj")
    case 6: 
        print("Czerwiec")
    case 7:
        print("Lipiec")
    case 8:
        print("Sierpien")
    case 9:
        print("Wrzesien")
    case 10:
        print("Pazdziernik")
    case 11:
        print("Listopad")
    case 12:
        print("Grudzien")
    case _:
        print("Nie wiem co to za miesiac")
        
match miesiac:
    case 12 | 1 | 2: 
        print("Zima")
    case 3 | 4 | 5:
        print("Wiosna")
    case 6 | 7 | 8 if miesiac%2 == 0:
        print ("Letnie miesiace z 30 dniami")
    case 9 | 10| 11:
        print("Jesien")
        
