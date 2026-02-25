

class Basel:
    def __init__(self):
        self.resolution=0.00000001

    def Calculate(self):
        prevBasel = []
        basel = 0
        n = 0
        cond = True

        while cond:
            n += 1
            basel += 1 / n ** 2
            prevBasel.append(basel)
            cond = self.Control(prevBasel, basel)
        return basel, n

    def Control(self,liste, bsl):
        cont=True
        if len(liste)==5:
            ort=0
            for i in liste:
                ort +=i
            ort =ort/len(liste)
            cont=abs(ort-bsl)>self.resolution
            liste.pop(0)
        return cont

basel0=Basel()
print(basel0.Calculate())

basel1=Basel()
basel1.resolution=0.0001
print(basel1.Calculate())