from abc import ABC, abstractmethod

# Absztrakt Auto osztály
class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def auto_info(self):
        pass

# Személyautó osztály
class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ulesek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ulesek_szama = ulesek_szama

    def auto_info(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Ülések száma: {self.ulesek_szama}, Díj: {self.berleti_dij} Ft/nap"

# Teherautó osztály
class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras_kg):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras_kg = teherbiras_kg

    def auto_info(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Teherbírás: {self.teherbiras_kg} kg, Díj: {self.berleti_dij} Ft/nap"

# Bérlés osztály
class Berles:
    def __init__(self, auto: Auto, datum: str):
        self.auto = auto
        self.datum = datum

    def berles_info(self):
        return f"{self.auto.rendszam} - {self.datum} - {self.auto.berleti_dij} Ft"

# Autókölcsönző
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

        # 5 személyautó
        self.autok.append(Szemelyauto("ABC-123", "Toyota Corolla", 10000, 5))
        self.autok.append(Szemelyauto("DEF-456", "Honda Civic", 11000, 5))
        self.autok.append(Szemelyauto("GHI-789", "Mazda 3", 10500, 5))
        self.autok.append(Szemelyauto("JKL-321", "Ford Focus", 9500, 5))
        self.autok.append(Szemelyauto("MNO-654", "Opel Astra", 9900, 5))

        # 5 teherautó
        self.autok.append(Teherauto("PQR-987", "Mercedes Sprinter", 15000, 1500))
        self.autok.append(Teherauto("STU-159", "Ford Transit", 14000, 1300))
        self.autok.append(Teherauto("VWX-753", "Iveco Daily", 16000, 1700))
        self.autok.append(Teherauto("YZA-852", "Renault Master", 14500, 1400))
        self.autok.append(Teherauto("BCD-951", "Volkswagen Crafter", 15500, 1600))

        # Előre rögzített 4 bérlés
        self.berlesek.append(Berles(self.autok[0], "2025-04-01"))
        self.berlesek.append(Berles(self.autok[5], "2025-04-02"))
        self.berlesek.append(Berles(self.autok[3], "2025-04-03"))
        self.berlesek.append(Berles(self.autok[7], "2025-04-04"))

    def listaz_autok(self):
        print("\nElérhető autók:")
        for auto in self.autok:
            if not any(b.auto == auto for b in self.berlesek):
                print(auto.auto_info())

    def auto_berlese(self, rendszam, datum):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                if any(b.auto == auto for b in self.berlesek):
                    print("Ez az autó már ki van bérelve!")
                    return
                self.berlesek.append(Berles(auto, datum))
                print(f"Sikeres bérlés! Ár: {auto.berleti_dij} Ft")
                return
        print("Nincs ilyen rendszámú autó!")

    def berles_lemondasa(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                self.berlesek.remove(berles)
                print("Bérlés lemondva.")
                return
        print("Nincs ilyen bérlés!")

    def listaz_berlesek(self):
        print("\nAktuális bérlések:")
        if not self.berlesek:
            print("Nincs aktív bérlés.")
        for berles in self.berlesek:
            print(berles.berles_info())

# Parancssoros felhasználói felület
def main():
    kolcsonzo = Autokolcsonzo("City Rent")

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ RENDSZER ---")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Aktuális bérlések listázása")
        print("0. Kilépés")
        valasztas = input("Választás: ")

        if valasztas == "1":
            kolcsonzo.listaz_autok()
        elif valasztas == "2":
            rendszam = input("Add meg a rendszámot: ")
            datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")
            kolcsonzo.auto_berlese(rendszam, datum)
        elif valasztas == "3":
            rendszam = input("Add meg a rendszámot: ")
            kolcsonzo.berles_lemondasa(rendszam)
        elif valasztas == "4":
            kolcsonzo.listaz_berlesek()
        elif valasztas == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
