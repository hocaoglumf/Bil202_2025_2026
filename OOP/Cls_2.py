class Shape:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_circle(cls):
        return cls("Circle")

    @classmethod
    def create_square(cls):
        return cls("Square")

    @classmethod
    def create_Shape(cls, name):
        return cls(name)

# Kullanım
s1 = Shape.create_circle()
s2 = Shape.create_square()
s3=Shape.create_Shape("Amorf")

print(s1.name)  # Circle
print(s2.name)  # Square
print(s3.name)