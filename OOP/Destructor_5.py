'''
Bu örnek, circular reference (döngüsel referans) problemini weakref ile nasıl çözdüğümüzü gösteriyor.


Amaç:

A ve B nesneleri birbirine referans veriyor
Ama bu referanslardan biri zayıf (weak) olduğu için döngü kırılıyor
Böylece nesneler düzgün şekilde silinebiliyor


weakref → referans sayısını artırmaz
Döngüleri kırar
Garbage collector’ın düzgün çalışmasını sağlar
__del__ güvenli şekilde çalışabilir

'''
import weakref

class A:
    def __init__(self):
        self.b = None

    def __del__(self):
        print("A is killed")

class B:
    def __init__(self):
        self.a = None


    def __del__(self):
        print("B is killed")


a = A()
b = B()

a.b = weakref.ref(b)  # zayıf referans
b.a = a


del a

del b

