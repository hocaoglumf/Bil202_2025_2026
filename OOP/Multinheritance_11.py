


class A:
    def show(self):
        print("A.show")


class B:
    def show(self):
        print("B.show")



class C(A, B):
    def show(self):
        print("C.show")
        A.show(self)
        B.show(self)


obj = C()
obj.show()