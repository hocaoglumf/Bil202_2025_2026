class Robot:
    populasyon = 0

    def __init__(self, isim):
        self.isim = isim
        Robot.populasyon += 1
        self.enerji = 100

    def hareket_et(self):
        print(f"{self.isim} hareket ediyor.")
        self.enerji -= 10

class Drone(Robot):
    def __init__(self, isim, kanat_sayisi):
        super().__init__(isim)
        self.kanat_sayisi = kanat_sayisi
        self.enerji = 200  # Enerjiyi güncelliyoruz

    def hareket_et(self):
        super().hareket_et()
        print(f"{self.isim} uçuyor (Kanat sayısı: {self.kanat_sayisi}).")
        self.enerji -= 20

# Nesnelerin oluşturulması
r1 = Robot("R2D2")
d1 = Drone("Bayraktar", 4)

# İşlemler
r1.hareket_et()
d1.hareket_et()

print(f"--- Sonuçlar ---")
print(f"R2D2 Enerji: {r1.enerji}")
print(f"Bayraktar Enerji: {d1.enerji}")
print(f"Toplam Robot Sayısı: {Robot.populasyon}")
