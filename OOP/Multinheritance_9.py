class A:
    def __init__(self, **kwargs):
        print("A init")
        super().__init__(**kwargs)

    def show(self):
        print("A show")


class B:
    def __init__(self, **kwargs):
        print("B init")
        super().__init__(**kwargs)

    def hello(self):
        print("B hello")


class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()


obj = C()
obj.show()
obj.hello()
print(C.mro())