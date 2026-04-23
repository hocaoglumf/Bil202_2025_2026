class A:
    def __str__(self):
        pass

    def Write(self,x):
        print(x)

class B(A):
    def __init__(self):
        pass

    def Write(self,x,y):
        print(x,"  ",y)

a=A()
b=B()

a.Write(2)
b.Write(3,4)
