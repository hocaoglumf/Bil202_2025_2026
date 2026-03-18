

class Student:
    totalAge=0
    numberofperson=0
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split("-")
        cls.totalAge +=int(age)
        cls.numberofperson +=1
        return cls(name, int(age))

    @classmethod
    def GetAverageAge(cls):
        return cls.totalAge/cls.numberofperson

# Kullanım
s1 = Student.from_string("Fatih-35")
s2 = Student.from_string("Ali-45")
s3 = Student.from_string("Fatma-25")
print(Student.from_string("Talip-15").name)

print(Student.GetAverageAge())

print(s1.name)  # Fatih
print(s1.age)   # 35