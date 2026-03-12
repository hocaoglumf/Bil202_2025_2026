import  Yardimcilar as y


class Matematic:
    results=[]
    def __init__(self):
        self.__myOwnResult=[]

    def Sin(self,X):
        s=y.Yardimcilar.Sin(X)
        self.__myOwnResult.append(s)
        return s

    def Cos(self,X):
        s=y.Yardimcilar.Cos(X)
        self.__myOwnResult.append(s)
        return s

    def Log(self,X,base):
        s=y.Yardimcilar.Log(X, base)
        self.__myOwnResult.append(s)
        return s

    def GetMyOwnResults(self):
        return self.__myOwnResult

a=Matematic()
Matematic.results.append(a.Cos(30))
print(Matematic.results, "My Own Results :", a.GetMyOwnResults() )

b=Matematic()
Matematic.results.append(b.Sin(30))
print(Matematic.results, "My Own Results :", b.GetMyOwnResults() )


c=Matematic()
Matematic.results.append(c.Cos(30))
print(Matematic.results, "My Own Results :", c.GetMyOwnResults() )


d=Matematic()
Matematic.results.append(d.Log(30,2))
print(Matematic.results, "My Own Results :", d.GetMyOwnResults() )

