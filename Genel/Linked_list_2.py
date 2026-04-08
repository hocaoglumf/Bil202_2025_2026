


import random

class Node:

    def __init__(self, Value):
        self.value=Value
        self.ref=None

    def Value(self):
        print(self.value)
        if not(self.ref==None):
            self.ref.Value()

liste=[]


for i in range(random.randint(10,20)):
    n=Node(random.randint(1,20))
    liste.append(n)


for i in range(1,len(liste)):
    liste[i-1].ref=liste[i]

liste[0].Value()