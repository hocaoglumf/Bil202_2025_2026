

def FuncYield():
    yield 1
    yield 2
    yield 3


f = FuncYield()

print(next(f))  # 1
print(next(f))  # 2
print(next(f))  # 3
