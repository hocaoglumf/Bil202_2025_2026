class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    def __init__(self):
        print("Constructor C")
        pass


obj = C()
obj.show()