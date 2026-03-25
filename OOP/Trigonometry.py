from abc import ABC, abstractmethod
import random
import math

import numpy as np
import matplotlib.pyplot as plt

class Trigonometry(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def GetValue(self, x):
        return None

class Sinus(Trigonometry):
    def GetValue(self, x):
        return math.sin(x)

class Cosinus(Trigonometry):
    def GetValue(self, x):
        return math.cos(x)

class Tanjant(Trigonometry):
    def GetValue(self, x):
        return math.tan(x)


class Cotanjant(Trigonometry):
    def GetValue(self, x):
        if math.tan(x)==0:
            return 1
        return 1/math.tan(x)


xaxis=[]
yaxis=[]
fncs=[Sinus(), Cosinus(), Tanjant(), Cotanjant(),Sinus(), Cosinus()]
for i in range(0,100):
    x=random.randint(0,360)
    if x==90 or x==270:
        print(x)
        x=0
    xaxis.append(x)

    s=fncs[random.randint(0,len(fncs)-1)]
    yaxis.append(s.GetValue(x))

for i in range(len(xaxis)-1):
    for j in range(i,len(xaxis)):
        if xaxis[i]>=xaxis[j]:
            xaxis[i],xaxis[j]=xaxis[j],xaxis[i]
            yaxis[i],yaxis[j]=yaxis[j],yaxis[i]

plt.plot(xaxis, yaxis)
plt.xlabel("x")
plt.ylabel("")
plt.title("")
plt.grid()

plt.show()