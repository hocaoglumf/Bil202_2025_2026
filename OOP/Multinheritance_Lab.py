
class Student:
    def __init__(self):
        pass


class Industrial(Student):
    pass

class ComputerEng(Student):
    pass


class CAP_IC(Industrial, ComputerEng):
    pass

class Electronic(Student):
    pass

class CAP_IE(Industrial, Electronic)
