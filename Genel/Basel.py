

def Basel():
    prevBasel=0
    basel=0
    n=0
    cond=True
    while cond:
        n +=1
        basel +=1/n**2
        cond=abs(prevBasel-basel)>0.00000001
        prevBasel=basel
    return basel, n

basel, n=Basel()

print("Basel:", basel, " İterasyon: ",n)