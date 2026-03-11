import math

class Geometri:
    def __init__(self):
        pass


class Ucgen(Geometri):
    def __init__(self):
        super().__init__()
        self.taban=0
        self.yukseklik=0

    def Alan(self):
        return self.taban*self.yukseklik/2

class Dortgen(Geometri):
    def __init__(self):
        super().__init__()
        self.a=0
        self.b=0

    def Alan(self):
        return self.a*self.b

class Daire(Geometri):
    def __init__(self):
        super().__init__()
        self.r = 0

    def Alan(self):
        return self.r**2  * math.pi


u0=Ucgen()
u0.taban=5
u0.yukseklik=3

u1=Ucgen()
u1.taban=2
u1.yukseklik=3

d0=Dortgen()
d0.a=5
d0.b=6

u2=Ucgen()
u2.taban=20
u2.yukseklik=12


d1=Dortgen()
d1.a=7
d1.b=6


dr=Daire()
dr.r=23

lst=[u0, u1, u2, d1, dr, d0]


for i in lst:
    print(type(i), "  ", i.Alan())
