liste=[3,2,3,4,5,2,3,4,5]

def FindMaks(liste):
    maks=liste[0]
    for i in liste:
        if maks<i:
            maks=i
    return maks

mks=FindMaks(liste)
print(mks)

