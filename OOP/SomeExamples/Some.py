class Some:
    param=5
    def mystery(self, a, b):
        if b == 0:
            return a
        return self.mystery(b, a % b)

    def wrapper(self,x):
        result = 0
        for i in range(1, x):
            result += self.mystery(i, x)
        return result

s=Some()
Some.param=16
d=Some()
print(s.wrapper(3)*d.param)

