
# Definicja klasy bazowej
class Papier:
    def __init__(self, rodzaj, gramatura, gladkosc):
        self.rodzaj = rodzaj
        self.gramatura = gramatura
        self.gladkosc = gladkosc

    def info(self):
        print(f"Papier {self.rodzaj} o gramaturze {self.gramatura} g/m²")

# Definicja klasy pochodnej
class Zeszyt(Papier):
    def __init__(self, rodzaj, gramatura, gladkosc, liczbaStron, wzorStrony, formatAB):
        super().__init__(rodzaj, gramatura, gladkosc)
        self.liczbaStron = liczbaStron
        self.wzorStrony = wzorStrony
        self.formatAB = formatAB

    def info(self):
        print("Ten zeszyt ma:")
        print(f" {self.liczbaStron} stron")
        super().info()
        print(f"Format: {self.formatAB}")
        print(f"Kartki: {self.wzorStrony} ")
        print(f"Papier o gramaturze: {self.gramatura}")
        
akwarelowy = Papier("akwarelowy", 300, "Rough")
akwarelowy.info()

doMatematyki = Zeszyt("zwykly",120, "gladki", 60, "w kratke", "A5" )
doMatematyki.info()

