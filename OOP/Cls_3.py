class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)


class Dog(Animal):
    pass


# Kullanım
d = Dog.create("Karabaş")

print(type(d))  # <class '__main__.Dog'>
print(d.name)

d2=Dog("Kujo")
print(type(d2))
print(d2.name)