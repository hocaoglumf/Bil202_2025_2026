import math
import matplotlib.pyplot as plt

class Trigonometry:
    def __init__(self):
        self.x=[]
        self.y=[]

    def Calculate(self):
        pass

    def WriteValues(self):
        print("x:", self.x)
        print("y:", self.y)


class Sinus(Trigonometry):
    def __init__(self):
        super().__init__()

    def Calculate(self):
        for i in range(0,360,10):
            self.x.append(i)
            self.y.append(math.sin(i))

class Cosinus(Trigonometry):
    def __init__(self):
        super().__init__()

    def Calculate(self):
        for i in range(0,360,10):
            self.x.append(i)
            self.y.append(math.cos(i))


class Tan(Trigonometry):
    def __init__(self):
        super().__init__()
        self.isim="Tanjant"

    def Calculate(self):
        for i in range(0,360,10):
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
        for i in self.trigoList:
            plt.plot(i.x,i.y)

        plt.show()


s0=Sinus()
s1=Sinus()
c0=Cosinus()
c1=Cosinus()
s2=Sinus()
tn0=Tan()
tn1=Tan()

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
