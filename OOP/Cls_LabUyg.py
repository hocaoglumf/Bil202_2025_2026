

class Student:
    listem=[]
    numberofStudents =0
    def __init__(self, name, number):
        self.name=name
        self.number=number


    def __str__(self):
        return f"İsim: {self.name}, No: {self.number} Actual # {str(Student.RegisteredStudentNumbers())} Registered # {str(Student.ActualStudentNumber())}"

    @classmethod
    def Create(cls, name, number):
        return cls(name,number)

    @classmethod
    def Add(cls, ogr):
        cls.numberofStudents +=1
        cls.listem.append(ogr)

    @classmethod
    def RemoveStudent(cls, ogr):
        cls.listem.remove(ogr)

    @classmethod
    def WriteClassList(cls):
        for i in cls.listem:
            print(i)

    @classmethod
    def ActualStudentNumber(cls):
        return len(cls.listem)

    @classmethod
    def RegisteredStudentNumbers(cls):
        return cls.numberofStudents

o1=Student.Create("Ali","1211321")
Student.Add(o1)


o2=Student.Create("Ayşe","0907621321")
Student.Add(o2)

o3=Student.Create("Ahmet","996721321")
Student.Add(o3)



Student.WriteClassList()

print("     ")

Student.RemoveStudent(o2)

Student.WriteClassList()



