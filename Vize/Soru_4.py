'''
Üç farklı işlem tanımlanacaktır. Bunlar Hip, Hop ve Zip olarak isimlendirilecektir.
Her biri için, verilen iki sayı arasında (a ve b) yürütülen hesaplama şu şekilde yapılmaktadır.

Hip: a + b – a*b, Hop: (a-b)/(a+b), Zip: ∑_(i=1)^b▒〖〖-1〗^i×a^i 〗

Bir listeye alınan nesnelere Hesapla dediğimizde hepsi kendi hesap yöntemine göre hesaplayıp sonuçları kendi sonuç özniteliğine atayacak.

'''


class Islem:
    def __init__(self):
        self.sonuc=0
    def Hesap(self,a,b):
        return 0


class Hip(Islem):
    def Hesap(self,a,b):
        self.sonuc=a+b-a*b
        return self.sonuc

class Hop(Islem):
    def Hesap(self,a,b):
        self.sonuc = (a-b)/(a+b)
        return  self.sonuc

class Zip(Islem):
    def Hesap(self,a,b):
        s=0
        for i in range(1,b+1):
           s +=(-1)**i*a**i
        self.sonuc=s
        return s

L=[Hip(), Hop(), Hip(), Zip(),  Hop(), Hip(), Zip(), Hip(), Zip()]

for i in L:
    print(i.Hesap(3,5))



