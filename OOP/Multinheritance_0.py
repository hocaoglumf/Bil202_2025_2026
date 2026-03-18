'''

Employee sınıfı:

Person sınıfından isim ile ilgili davranışları,

Worker sınıfından maaş ile ilgili davranışları alır.
'''


class Person:
    def set_name(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


class Worker:
    def set_salary(self, salary):
        self.salary = salary

    def show_salary(self):
        print(f"Salary: {self.salary}")


class Employee(Person, Worker):
    pass


e = Employee()
e.set_name("Ali")
e.set_salary(50000)

e.show_name()
e.show_salary()