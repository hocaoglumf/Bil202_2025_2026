'''

Multiple inheritance’ta en önemli konulardan biri super() kullanımıdır.

Yanlış bir kullanım, bazı üst sınıfların constructor’larının hiç çalışmamasına yol açabilir.

Aşağıdaki kod doğru çalışır fakat büyük sistemlerde bu yöntem önerilmez. Çünkü zinciri elle yönetmek hata üretir.
'''


class A:
    def __init__(self):
        print("A init")


class B:
    def __init__(self):
        print("B init")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C init")


obj = C()