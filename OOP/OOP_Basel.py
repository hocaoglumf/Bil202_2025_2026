

class Basel:
    def __init__(self):
        self.resolution=0.00000001

    def Calculate(self):
        prevBasel = 0
        basel = 0
        n = 0
        cond = True
        while cond:
            n += 1
            basel += 1 / n ** 2
            cond = abs(prevBasel - basel) > self.resolution
            prevBasel = basel
        return basel, n


basel0=Basel()
print(basel0.Calculate())

basel1=Basel()
basel1.resolution=0.0001
print(basel1.Calculate())