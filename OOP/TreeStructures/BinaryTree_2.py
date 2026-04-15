'''


'''

class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.value=0


    def Expand(self,L):
        if self.left==None:
            g=Node()
            g.value=L[0]
            self.left=g
        else:
            self.left.Expand(L)

        if self.right==None:
            g=Node()
            g.value=L[1]
            self.right=g
        else:
            self.right.Expand(L)


root=Node()

root.Expand([0,1])

root.Expand([2,3])

root.Expand([4,5])

print(root)



