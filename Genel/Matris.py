'''
Verilen matris elemanlarından tek sayıları ve çift sayıları ayrı ayrı
toplayan ve bir dictionary'e ekleyen kod.
'''

m=[[1,2,3,2,6],
   [3,2,4,3,5],
   [5,4,2,6,0]]

tekTpl, cftTpl=0,0
D={}
for i in m:
    for j in i:
        if j %2 ==0:
            cftTpl +=j
        else:
            tekTpl +=j

D["tek"]=tekTpl
D["cift"]=cftTpl

print(list(D.keys()))
print(list(D.values()))
print(D)
