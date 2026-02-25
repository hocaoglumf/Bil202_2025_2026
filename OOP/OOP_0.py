'''
Bir class en basit haliyele nasıl tanımlanır.
'''
class insan:
    def __init__(self):
        self.ad=""


    def isim(self):
        print(self.ad)


print(insan)

def Yaz(x):
    return x

print(Yaz(2))
print(Yaz)

'''
a0 ve a1 insan sınıfından alınan nesnelerdir (instances). 
'''
a0=insan()
a1=insan()
print(a0)


'''
a0 nesnesinin ad özniteliğine "Ali" değeri atanmıştır. 
'''
a0.ad="Ali"


'''
a1 nesnesinin ad özniteliğine "Veli" değeri atanmıştır. 
'''
a1.ad="Veli"

a0.isim()
