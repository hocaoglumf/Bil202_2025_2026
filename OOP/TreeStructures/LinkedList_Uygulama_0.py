
import random

class LinkedList:
    counter=0
    iteration=0
    def __init__(self):
        self.ref=None
        self.value=random.randint(1,10)

    def Sum(self):
        LinkedList.counter +=1
        if LinkedList.counter==LinkedList.iteration:
            return self.value

        if not(self.ref==None):
            self.value +=self.ref.Sum()
        return self.value

class Container:
    def __init__(self):
        self.liste=[]

    def Create(self,N):
        for i in range(N):
            if len(self.liste) > 0:
                a = LinkedList()
                a.ref = self.liste[i - 1]
                self.liste.append(a)
            else:
                a = LinkedList()
                self.liste.append(a)

        self.liste[0].ref = self.liste[len(self.liste) - 1]


    def Play(self):
        LinkedList.counter, LinkedList.iteration =0,0
        n=random.randint(0,len(self.liste)-1)
        LinkedList.iteration=random.randint(10,100)

        print("N:",n, " iteration:", LinkedList.iteration)
        print(self.liste[n].Sum())


container=Container()
container.Create(10)
container.Play()



