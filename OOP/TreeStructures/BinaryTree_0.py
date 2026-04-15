'''

İkili Ağaçlarda (Binary tree) iki alt düğüm vardır. Pratikte left, right diye isimlendirebiliriz.

'''

class Node:
    def __init__(self):
        self.left=None
        self.right=None



    def SetLeft(self, l):
        self.left=l

    def SetRight(self,r):
        self.right=r




root=Node()

lft=Node()

rght=Node()

root.SetLeft(lft)

root.SetRight(rght)

