class A:
    def greet(self):
        print("Merhaba A")


class B:
    def greet(self):
        print("Merhaba B")


class C(A, B):
    pass


c = C()
c.greet()

