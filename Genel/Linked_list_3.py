'''
Bu sınav çok kolay olacak

'''


class Ogrenci:
    def __init__(self):
        self.linkedObj=None

    def Soyle(self, soz):
        print(soz)
        if (self.linkedObj==None):
            print("Çok da kolay olmadı")
        else:
            self.linkedObj.Soyle(soz)

class Sinif:
    def __init__(self):
        self.sinif=[]

    def Ekle(self,e):
        if len(self.sinif)>0:
            self.sinif[len(self.sinif)-1].linkedObj=e
        self.sinif.append(e)

    def Soyle(self,soz):
        self.sinif[0].Soyle(soz)

o0=Ogrenci()
o1=Ogrenci()
o2=Ogrenci()
o3=Ogrenci()


snf=Sinif()
snf.Ekle(o0)
snf.Ekle(o1)
snf.Ekle(o2)
snf.Ekle(o3)

snf.Soyle("Bu sınav çok kolay olacak .")
