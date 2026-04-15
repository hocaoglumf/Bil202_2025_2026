'''



'''


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value=0
        self.name=""

    def SetLeft(self, l):
        self.left = l

    def SetRight(self, r):
        self.right = r

    def SetValue(self,v):
        self.value=v

    def Print(self):
        print("İsim:", self.name, "Değer:", self.value)
        if not(self.left==None):
            self.left.Print()

        if not(self.right==None):
            self.right.Print()

    def SetName(self,n):
        self.name=n

root = Node()
root.SetName("Kök")
root.SetValue(0)



lft = Node()

lft.SetName("Sol0")
lft.SetValue(1)

rght = Node()
rght.SetName("Sag0")
rght.SetValue(2)

root.SetLeft(lft)

root.SetRight(rght)


root.Print()


