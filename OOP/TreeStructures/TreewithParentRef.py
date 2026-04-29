

class Node:
    def __init__(self):
        self.branches=[]
        self.parent=None


    def Add(self,n):
        n.parent=self
        self.branches.append(n)




root=Node()

c0=Node()
c1=Node()
c2=Node()
c3=Node()
c4=Node()
c5=Node()

root.Add(c0)
root.Add(c1)
root.Add(c2)

c0.Add(c3)
c0.Add(c4)
c1.Add(c5)

