'''

Parametreli multiple inheritance örneği


Burada:

Employee, Person ve Worker sınıflarını birleştiriyor

super() zincirini bozmamak için **kwargs kullanılıyor

her sınıf kendi parametresini alıp kalanları aşağı geçiriyor

Bu yapı, multiple inheritance’ta çok kullanışlıdır.


Neden **kwargs kullanıyoruz?

Çünkü her üst sınıf farklı parametre bekleyebilir.

Örneğin:

Person → name

Worker → salary

Her sınıf yalnızca kendine ait olanı alır, kalanları super() ile bir sonraki sınıfa iletir.

'''

class Person:
    def __init__(self, name, **kwargs):
        self.name = name
        print(f"Person init: {self.name}")
        super().__init__(**kwargs)


class Worker:
    def __init__(self, salary, **kwargs):
        self.salary = salary
        print(f"Worker init: {self.salary}")
        super().__init__(**kwargs)


class Employee(Person, Worker):
    def __init__(self, name, salary):
        print("Employee init")
        super().__init__(name=name, salary=salary)


e = Employee("Ayşe", 60000)
print(e.name)
print(e.salary)
print(Employee.mro())