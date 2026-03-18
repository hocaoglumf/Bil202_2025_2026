'''
Neden sadece A çalıştı?

Çünkü C(A, B) yazdığımızda Python önce A’ya bakar. C içinde __init__ yoksa, sırayla ilk bulduğu __init__ metodunu kullanır.
'''
class A:
    def __init__(self):
        print("A constructor")


class B:
    def __init__(self):
        print("B constructor")


class C(A, B):
    pass


obj = C()

''' 
Method Resolution Order (MRO) 

Metot çağrım sıralamasını gösterir.

'''
print(C.__mro__)