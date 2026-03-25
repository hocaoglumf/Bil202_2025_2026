'''
Circular Reference Problem

Circular Reference (Döngüsel Referans) Problemi,
Python’da iki veya daha fazla nesnenin birbirine referans vermesi durumudur.
Bu durum, özellikle __del__ (destructor) kullanıldığında beklenmeyen davranışlara yol açabilir.

Python bu nesneleri güvenli şekilde yok edemeyebilir

Çünkü:
Hangi sırayla silineceği belirsiz
Bir nesne silinirken diğeri hâlâ ona ihtiyaç duyabilir

Sonuç:
__del__ hiç çağrılmayabilir
Bellek sızıntısı (memory leak) oluşabilir

Çözüm için weakRef (Destructor_5) örneğine bakınız.
'''

class A:
    def __init__(self):
        self.b = None

    def __del__(self):
        print("A destroyed")

class B:
    def __init__(self):
        self.a = None

    def __del__(self):
        print("B destroyed")

a = A()
b = B()

a.b = b
b.a = a

del a
del b