class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


class GraduateStudent(Student):
    pass

g = GraduateStudent.from_string("Ayşe-30")