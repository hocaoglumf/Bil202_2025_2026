

#iterayon ile

def Iteration(n):
    f=1
    for i in range(1,n+1):
        f *=i

    print(n,"! =",f)
    return f


#recursive özyinelemeli


def Recursive(n):
    if n==0:
        return 1
    return n*Recursive(n-1)

Iteration(5)

print(Recursive(5))
