'''

Super çağrımında doğru yaklaşım.

'''

class A:
    def __init__(self):
        print("A init")
        super().__init__()


class B:
    def __init__(self):
        print("B init")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()


obj = C()
print(C.mro())