'''

Hesaplanan basel değerleri her 100 adımda bir listeye eklendi.
'''

def Basel():
    prevBasel=0
    basel=0
    n=0
    cond=True
    yuzlukadimler=[]
    while cond:
        n +=1
        if n%100==0:
            yuzlukadimler.append(basel)
        basel +=1/n**2
        cond=abs(prevBasel-basel)>0.00000001
        prevBasel=basel
    return basel, n, yuzlukadimler

basel, n, adimlar=Basel()

print("Basel:", basel, " İterasyon: ",n, "  Yüzlük Liste", adimlar)

for i in adimlar:
    print(i)