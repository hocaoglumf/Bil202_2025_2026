
def ListeTopla(L):
    t=0
    for i in L:
        t +=i
    return t

m=[[1,2,3,2,6],
   [3,2,4,3,5],
   [5,4,2,6,0]]

for i in range(len(m)):
    t=ListeTopla(m[i])
    print(i+1,". Satır Toplamı",t)