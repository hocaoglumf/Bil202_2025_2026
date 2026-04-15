

class Tree:
    def __init__(self):
        self.subnodes=[]
        self.value=0

    def Print(self):
        print(self.value)
        for i in self.subnodes:
            i.Print()



root=Tree()

n0=Tree()
n0.value=1

n1=Tree()
n1.value=2

n2=Tree()
n2.value=3

n3=Tree()
n3.value=4


root.subnodes.append(n0)
root.subnodes.append(n1)
root.subnodes.append(n2)
root.subnodes.append(n3)

root.Print()

