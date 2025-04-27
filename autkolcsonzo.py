from abc import ABC, abstractmethod
from datetime import date

# --- Absztrakt autó osztály ---
class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def auto_info(self):
        pass


# --- Személyautó osztály ---
class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ulesek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ulesek_szama = ulesek_szama

    def auto_info(self):
        return f"Személyautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Ülések: {self.ulesek_szama}, Díj: {self.berleti_dij} Ft/nap"


# --- Teherautó osztály ---
class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teherbiras_kg):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teherbiras_kg = teherbiras_kg

    def auto_info(self):
        return f"Teherautó | Rendszám: {self.rendszam}, Típus: {self.tipus}, Teherbírás: {self.teherbiras_kg} kg, Díj: {self.berleti_dij} Ft/nap"


# --- Bérlés osztály ---
class Berles:
    def __init__(self, auto, datum: date):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"{self.auto.rendszam} | {self.auto.tipus} | {self.datum} | {self.auto.berleti_dij} Ft"


# --- Autókölcsönző osztály ---
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_hozzaadas(self, auto):
        self.autok.append(auto)

    def auto_berlese(self, rendszam, datum):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return "❌ Nincs ilyen rendszámú autó."

        if any(b.auto.rendszam == rendszam and b.datum == datum for b in self.berlesek):
            return "❌ Az autó már bérlés alatt áll ezen a napon."

        uj_berles = Berles(auto, datum)
        self.berlesek.append(uj_berles)
        return f"✅ Bérlés sikeres. Ár: {auto.berleti_dij} Ft"

    def berles_lemondas(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                return "✅ Bérlés lemondva."
        return "❌ Nem található ilyen bérlés."

    def listaz_berlesek(self):
        if not self.berlesek:
            return "ℹ️ Nincsenek aktív bérlések."
        return "\n".join(str(b) for b in self.berlesek)

    def listaz_autok(self):
        return "\n".join(a.auto_info() for a in self.autok)


# --- Konzolos felhasználói interfész ---
def main():
    kolcsonzo = Autokolcsonzo("CityCar Rent")

    # Előre feltöltött autók
    kolcsonzo.auto_hozzaadas(Szemelyauto("ABC123", "Toyota Corolla", 10000, 5))
    kolcsonzo.auto_hozzaadas(Teherauto("DEF456", "Ford Transit", 15000, 1200))
    kolcsonzo.auto_hozzaadas(Szemelyauto("GHI789", "VW Golf", 11000, 5))

    # Előre feltöltött bérlések
    kolcsonzo.auto_berlese("ABC123", date(2025, 4, 13))
    kolcsonzo.auto_berlese("DEF456", date(2025, 4, 14))
    kolcsonzo.auto_berlese("GHI789", date(2025, 4, 15))
    kolcsonzo.auto_berlese("ABC123", date(2025, 4, 16))

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ RENDSZER ---")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Aktuális bérlések listázása")
        print("0. Kilépés")
        valasz = input("Választás: ")

        if valasz == "1":
            print("\n-- Elérhető autók --")
            print(kolcsonzo.listaz_autok())

        elif valasz == "2":
            rendszam = input("Rendszám: ").upper()
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                ev, ho, nap = map(int, datum.split("-"))
                datum_obj = date(ev, ho, nap)
                print(kolcsonzo.auto_berlese(rendszam, datum_obj))
            except ValueError:
                print("❌ Hibás dátumformátum.")

        elif valasz == "3":
            rendszam = input("Rendszám: ").upper()
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
            try:
                ev, ho, nap = map(int, datum.split("-"))
                datum_obj = date(ev, ho, nap)
                print(kolcsonzo.berles_lemondas(rendszam, datum_obj))
            except ValueError:
                print("❌ Hibás dátumformátum.")

        elif valasz == "4":
            print("\n-- Aktuális bérlések --")
            print(kolcsonzo.listaz_berlesek())

        elif valasz == "0":
            print("👋 Viszlát!")
            break

        else:
            print("❗ Érvénytelen opció.")


if __name__ == "__main__":
    main()
