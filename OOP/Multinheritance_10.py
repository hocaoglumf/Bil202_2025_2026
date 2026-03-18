class A:
    def show(self):
        print("A.show çalıştı")


class B:
    def show(self):
        print("B.show çalıştı")



class C(A, B):
    def call_both(self):
        A.show(self)
        B.show(self)





obj = C()
obj.show()

A.show(obj)
B.show(obj)


obj = C()
obj.call_both()

