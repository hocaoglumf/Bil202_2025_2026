import time


memo ={0 :1 ,1 :1}
def FibonacciDinamic(n):
    if n in memo:
        return memo[n]
    else:
        memo[n]=FibonacciDinamic(n-1) + FibonacciDinamic(n-2)
    return memo[n]


def Fibonacci(n):
    if n<=2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

baslangic = time.perf_counter()
print(Fibonacci(4), memo)
print(Fibonacci(6), memo)
print(Fibonacci(12), memo)
print(Fibonacci(42), memo)
bitis = time.perf_counter()

print(f"Geçen süre: {bitis - baslangic:.6f} saniye")

baslangic = time.perf_counter()
print(FibonacciDinamic(4), memo)
print(FibonacciDinamic(6), memo)
print(FibonacciDinamic(12), memo)
print(FibonacciDinamic(42), memo)
bitis = time.perf_counter()
print(f"Geçen süre: {bitis - baslangic:.6f} saniye")