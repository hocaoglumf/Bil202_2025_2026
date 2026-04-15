'''

Kök düğüm kendi değerine left ve right düğümlerin değerlerini ekler ve yazar.

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



    def Process(self):
        if not(self.left==None): # self ve right her ikisi de aynı anda none veya none değil birini kontrol yeterli.
            self.value +=self.left.value+self.right.value
            print(self.value)
            self.left.Process()
            self.right.Process()
        else:
            print("Bitti")


root=Node()

root.Expand([0,1])

root.Expand([2,3])

root.Expand([4,5])


root.Process()


