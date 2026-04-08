'''

Bir soyut personel sınıfı hazırlayacaksınız. Sınıftan Isci ve Memur sınıfları türeteceksiniz. Bulunması gereken öznitelikler şunlar olacaktır.
İsim, soy isim, sicil no, saat ücreti, doğum tarihi ve doğum yeri. Memur ve işçiler farklı ücret hesaplama prosedürüne sahiptir.
İşçiler için ayrıca yıpranma katsayısı vardır ve ücret hesabında “çalışma süresi x saat ücretine x yıpranma katsayısı” şeklinde uygulanır.
Memurlarda böyle bir katsayı yoktur. Gerekli kodu yazınız.
'''


from abc import ABC, abstractmethod

class Personel(ABC):
    def __init__(self):
        self.isim=""
        self.soyisim=""
        self.dogumtarihi=""
        self.dogumYeri=""
        self.saatUcreti=0
        self.sicil=""

    @abstractmethod
    def Ucret(self, saat):
        return 0

class Memur(Personel):
    def __init__(self):
        super().__init__()

    def Ucret(self,saat):
        return self.saatUcreti*saat


class Isci(Personel):
    def __init__(self):
        super().__init__()
        self.yipranma=2

    def Ucret(self,saat):
        return self.saatUcreti*saat*self.yipranma


