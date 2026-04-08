


class Node:

    def __init__(self, Value):
        self.value=Value
        self.ref=None

    def Value(self):
        print(self.value)
        if not(self.ref==None):
            self.ref.Value()


n0=Node(0)
n1=Node(1)
n2=Node(2)
n3=Node(3)


n0.ref=n1
n1.ref=n2
n2.ref=n3

n0.Value()

