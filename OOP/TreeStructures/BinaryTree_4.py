'''
Alt düğümler parent düğümü biliyor

'''



class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.parent=None



    def SetLeft(self, l):
        self.left=l
        l.parent=self

    def SetRight(self,r):
        self.right=r
        r.parent=self




root=Node()

lft=Node()

rght=Node()

root.SetLeft(lft)

root.SetRight(rght)


print(lft.parent)

