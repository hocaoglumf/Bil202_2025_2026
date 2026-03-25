'''
Bu kod, Python’da bir sınıfın oluşturulma (constructor) ve yok edilme (destructor)
süreçlerini göstermek için yazılmış basit bir örnektir.


__del__ komutu p değişkenini siler.

Nesneye olan referans kaldırılır.

'''


class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")

p = Person("Ali")
del p

