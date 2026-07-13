class Test:
    a = None
    b = None

    def __init__(self, a):
        self.a = a
        self._x = 235
        self.__y = 457
        b = 'meow'

t=Test(2)

print(t.a)
print(Test.a)

Test.a=3
p=Test(5)

print(p.a)
print(Test.a)

Test.a=5

print(Test.a)
