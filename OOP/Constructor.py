
class Ogrenci:
    def __init__(self, name, no, dept):
        self.name=name
        self.no=no
        self.department=dept

    def Info(self):
        print("İsim :",self.name)
        print("Numara:", self.no)
        print("Bölüm: ",self.department)


ogr0=Ogrenci("Ali","2345", "Endüstri")
ogr0.Info()