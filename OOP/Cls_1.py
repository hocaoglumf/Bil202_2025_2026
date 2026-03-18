

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split("-")
        return cls(name, int(age))


# Kullanım
s1 = Student.from_string("Fatih-35")

print(s1.name)  # Fatih
print(s1.age)   # 35