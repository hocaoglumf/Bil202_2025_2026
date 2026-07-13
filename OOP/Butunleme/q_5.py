class KargoPaketi:
    sabit_hizmet_bedeli = 50

    def __init__(self, gonderici, agirlik):
        self.gonderici = gonderici
        self.agirlik = agirlik

    def agirlik_ekle(self, miktar):
        self.agirlik += miktar

    def toplam_maliyet(self):
        # Maliyet: Ağırlık başına 10 TL + Sabit Hizmet Bedeli
        return (self.agirlik * 10) + KargoPaketi.sabit_hizmet_bedeli


class VIPKargoPaketi(KargoPaketi):
    sabit_hizmet_bedeli = 120

    def __init__(self, gonderici, agirlik, sigorta_turu):
        super().__init__(gonderici, agirlik)
        self.sigorta_turu = sigorta_turu

    def agirlik_ekle(self, miktar):
        super().agirlik_ekle(miktar * 2)

    def toplam_maliyet(self):
        return (self.agirlik * 10) + self.sabit_hizmet_bedeli


k1 = KargoPaketi("Ahmet", 10)
v1 = VIPKargoPaketi("Mehmet", 20, "Tam Güvence")

k1.agirlik_ekle(5)
v1.agirlik_ekle(5)

KargoPaketi.sabit_hizmet_bedeli = 80

print(k1.toplam_maliyet())
print(v1.toplam_maliyet())
print(KargoPaketi.sabit_hizmet_bedeli)
print(VIPKargoPaketi.sabit_hizmet_bedeli)
