

class Tree:
    def __init__(self):
        self.subnodes=[]
        self.value=0

    def Add(self,L):
        if len(self.subnodes)>0:
            for i in self.subnodes:
                i.Add(L)
        else:
            for i in L:
                d=Tree()
                d.value=i
                self.subnodes.append(d)

    def Process(self):
        if len(self.subnodes)>0:
            for i in self.subnodes:
                self.value +=i.value

    def Print(self):
        print(self.value)
        if (len(self.subnodes)>0):
            for i in self.subnodes:
                i.Print()

root=Tree()

root.Add([0,1,2])
root.Add([5,4])
root.Add([2,3,6,4])
root.Add([-5,-4,0,-3])



for i in  range(4):
    root.Print()
    root.Process()
    print("-------------------")
