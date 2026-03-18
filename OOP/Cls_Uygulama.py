class Student:
    school_name = "Istanbul Medeniyet University"

    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, GPA: {self.gpa}, School: {Student.school_name}")

    # 🔹 classmethod: alternatif constructor
    @classmethod
    def from_string(cls, student_str):
        # "Ali,23,3.5"
        name, age, gpa = student_str.split(",")
        return cls(name, int(age), float(gpa))

    # 🔹 classmethod: sınıf seviyesinde işlem
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # 🔹 staticmethod: bağımsız yardımcı fonksiyon
    @staticmethod
    def is_passing(gpa):
        return gpa >= 2.0


# 🔹 Normal kullanım
s1 = Student("Ayşe", 22, 3.2)
s1.display()

# 🔹 classmethod ile nesne oluşturma
s2 = Student.from_string("Mehmet,24,2.8")
s2.display()

# 🔹 classmethod ile sınıf değişkenini değiştirme
Student.change_school("Bogazici University")

s1.display()
s2.display()

# 🔹 staticmethod kullanımı
print("Ayşe geçti mi?", Student.is_passing(s1.gpa))