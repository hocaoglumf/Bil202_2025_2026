

class Tree:
    liste = []
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

    def DepthSumRoot(self):
        self.DepthSum(self.value)

    def DepthSum(self,vl):
        if len(self.subnodes)>0:
            for i in self.subnodes:
                i.DepthSum(i.value +vl)
        else:
            self.value +=vl
            return self.value

    def WriteTree(self):
        print(self.value)
        for i in self.subnodes:
            i.WriteTree()


    def WriteLeaf(self):
        if len(self.subnodes)==0:
            Tree.liste.append(self.value)
            print(self.value)
        else:
            for i in self.subnodes:
                i.WriteLeaf()

root=Tree()
root.value=9

root.Add([0,1,2])
root.Add([5,4])
root.Add([2,3,6,4])
root.Add([-5,-4,0,-3])



root.DepthSumRoot()


print("-----------------")

#root.WriteTree()

print("*******************")

root.WriteLeaf()
print(Tree.liste)
print(max(Tree.liste))
