
class Employee:
    company_bonus = 1000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

    def total_income(self):
        return self.salary + Employee.company_bonus


class Manager(Employee):
    company_bonus = 2000

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def increase_salary(self, amount):
        super().increase_salary(amount * 2)

    def total_income(self):
        return self.salary + self.company_bonus


e1 = Employee("Ali", 5000)
m1 = Manager("Ayşe", 8000, "IT")

e1.increase_salary(500)
m1.increase_salary(500)

Employee.company_bonus = 1500

print(e1.total_income())
print(m1.total_income())
print(Employee.company_bonus)
print(Manager.company_bonus)
