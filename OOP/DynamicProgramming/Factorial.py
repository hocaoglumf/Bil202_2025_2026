
import time



class Factorial:
    def __init__(self):
        self.fct={0:1}

    def Factorial(self,n):
        baslangic = time.perf_counter()
        p=self.__Factorial_aux(n)
        bitis = time.perf_counter()
        return p, bitis - baslangic

    def FactorialDynamic(self,n):
        baslangic = time.perf_counter()
        p=self.__FactorialDynamic_aux(n)
        bitis = time.perf_counter()
        return p, bitis - baslangic

    def __Factorial_aux(self, n):
        if n==0:
            return 1
        return n*self.__Factorial_aux(n-1)

    def __FactorialDynamic_aux(self,n):
        if n in list(self.fct.keys()):
            return self.fct[n]

        self.fct[n]=n*self.__FactorialDynamic_aux(n-1)
        return self.fct[n]


f=Factorial()
n=40
val,dur=f.Factorial(n)
print("Standart Hesap:", n, "-->",val, " duration: ", dur)
n=42
val,dur=f.Factorial(n)
print("Standart Hesap:",  n, "-->",val, " duration: ", dur)

print()
n=40
val,dur=f.FactorialDynamic(n)
print("Dynamic Hesap:",  n, "-->",val, " duration: ", dur)
n=42
val,dur=f.FactorialDynamic(n)
print("Standart Hesap:",  n, "-->",val, " duration: ", dur)
print(f.fct)
print()
f.FactorialDynamic(43)

f.FactorialDynamic(4)

f0=Factorial()
f0.FactorialDynamic(43)