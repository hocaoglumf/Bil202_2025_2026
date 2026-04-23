
class Arac:
    teker_sayisi = 4

    def __init__(self, marka):
        self.marka = marka

oto1 = Arac("Tesla")
oto2 = Arac("Toyota")
oto2.teker_sayisi = 3

print(oto1.teker_sayisi)
print(oto2.teker_sayisi)
print(Arac.teker_sayisi)
