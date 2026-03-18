import  Yardimcilar as y


class Matematic:
    results=[]
    def __init__(self):
        self.__myOwnResult=[]

    def Sin(self,X):
        s=y.Yardimcilar.Sin(X)
        return s

    def Cos(self,X):
        s=y.Yardimcilar.Cos(X)
        return s

    def Log(self,X,base):
        s=y.Yardimcilar.Log(X, base)
        return s

    def GetMyOwnResults(self):
        return self.__myOwnResult

    def AddOwnResult(self, v):
        self.__myOwnResult.append(v)

    @classmethod
    def Add(cls, n, val):
        cls.results.append(val)
        n.AddOwnResult(val)




a=Matematic()
Matematic.Add(a,5)
Matematic.Add(a,a.Cos(30))
print(Matematic.results, "My Own Results :", a.GetMyOwnResults() )

b=Matematic()
Matematic.Add(b,b.Sin(30))
print(Matematic.results, "My Own Results :", b.GetMyOwnResults() )


c=Matematic()
Matematic.Add(c,c.Cos(30))
print(Matematic.results, "My Own Results :", c.GetMyOwnResults() )


d=Matematic()
Matematic.results.append(d.Log(30,2))
print(Matematic.results, "My Own Results :", d.GetMyOwnResults() )


