


class Base:
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def __str__(self):
        return "a:"+str(self.a)+"  b:"+str(self.b)

class FromBase(Base):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c

    def __str__(self):
        return "a:"+str(self.a)+"  b:"+str(self.b)+" c:"+str(self.c)

a=Base(1,2)
b=FromBase(5,6,7)

print(b)
print(a)