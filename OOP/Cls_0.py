


class Person:
    population = 0  # sınıf değişkeni

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population


# Kullanım
p1 = Person("Ali")
p2 = Person("Ayşe")
p3 = Person("Fatma")

print("Population: ", Person.get_population())  # 2
