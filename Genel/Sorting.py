'''
Verilen bir listeyi küçükten büyüğe sıralayan kod.
'''


def Sort(liste):
    for i in range(len(liste)-1):
        for j in range(i+1,len(liste)):
            if liste[i]>liste[j]:
                liste[i],liste[j]=liste[j],liste[i]

    return liste


#liste=[4,5,1,3,2,4,56,6]
#liste2=[9,7,5,0,2,2,5,7]
#print(Sort(liste))

#print(Sort(liste2))
