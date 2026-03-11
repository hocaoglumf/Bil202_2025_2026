import math
import matplotlib.pyplot as plt


class Trigonometry:
    def __init__(self):
        self.x=[]
        self.y=[]
        self.first=0
        self.last=360
        self.step=5

    def Calculate(self):
        pass

    def WriteValues(self):
        print("x:", self.x)
        print("y:", self.y)


class Sinus(Trigonometry):
    def __init__(self):
        super().__init__()

    def Calculate(self):
        for i in range(self.first,self.last,self.step):
            self.x.append(i)
            self.y.append(math.sin(i))

class Cosinus(Trigonometry):
    def __init__(self):
        super().__init__()

    def Calculate(self):
        for i in range(self.first,self.last,self.step):
            self.x.append(i)
            self.y.append(math.cos(i))


class Tan(Trigonometry):
    def __init__(self):
        super().__init__()
        self.isim="Tanjant"

    def Calculate(self):
        for i in range(self.first,self.last,self.step):
            self.x.append(i)
            self.y.append(math.tan(i))



class Bag:
    def __init__(self):
        self.trigoList=[]

    def AddObject(self,object):
        self.trigoList.append(object)

    def Call(self):
        for i in self.trigoList:
            i.Calculate()
            i.WriteValues()

    def Plot(self):
        plt.legend()
        for i in self.trigoList:
            plt.plot(i.x,i.y)

        plt.show()


s0=Sinus()

s1=Sinus()
s1.first=120
s1.last=320

c0=Cosinus()
c0.first=110
c0.last=320
c0.step=10

c1=Cosinus()
s2=Sinus()
tn0=Tan()
tn1=Tan()
tn1.first=60
tn1.last=120
tn1.step=1

bg=Bag()

bg.AddObject(s0)
bg.AddObject(s1)
bg.AddObject(s2)
bg.AddObject(c1)
bg.AddObject(c0)
bg.AddObject(tn0)
bg.AddObject(tn1)

bg.Call()
bg.Plot()
