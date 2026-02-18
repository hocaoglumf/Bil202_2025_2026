'''
verilen matrisin her bir satırını sıralayıp ayrı bir matris yapan kod.
'''


import Sorting as srt

m=[[1,2,3,2,6],
   [3,2,4,3,5],
   [5,4,2,6,0]]

mnew=[]
for i in m:
    l=srt.Sort(i)
    mnew.append(l)

for i in mnew:
    print(i)