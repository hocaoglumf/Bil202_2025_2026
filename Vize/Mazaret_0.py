class Harf:
    counter=0
    def __init__(self):
        self.ref=None

class A(Harf):

    def Yaz(self):
        print("A")
        Harf.counter +=1
        if Harf.counter==5:
            return
        self.ref.Yaz()

class B(Harf):

    def Yaz(self):
        print("B")
        Harf.counter +=1
        if Harf.counter==5:
            return
        self.ref.Yaz()
a=A()
b=B()
a.ref=b
b.ref=a

try:
    a.Yaz()
except:
    print("hata")
