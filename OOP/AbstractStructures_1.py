from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):

    def move(self):
        print(f"{self.name} is driving")

c=Car("Murat124")
c.move()