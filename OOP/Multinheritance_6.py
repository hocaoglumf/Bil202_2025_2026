'''

Diamond problemi


    A
   / \
  B   C
   \ /
    D


Çok önemli nokta

A.__init__() bir kez çalışır.

İşte super()’ın en büyük avantajı burada ortaya çıkar. Eğer elle A.__init__() çağırıyor olsaydık, aynı constructor iki kez çalışabilirdi.

'''

class A:
    def __init__(self):
        print("A init")
        super().__init__()


class B(A):
    def __init__(self):
        print("B init")
        super().__init__()


class C(A):
    def __init__(self):
        print("C init")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()


d = D()
print(D.mro())