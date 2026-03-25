from abc import ABC, abstractmethod
import random

class Animal(ABC):  # Soyut Sınıf (Abstract class)

    @abstractmethod
    def speak(self):
        pass

    def sleep(self):  # Somut metot (Concrete method)
        print("Sleeping...")


class Dog(Animal):

    def speak(self):
        print("Bark")

class Cat(Animal):

    def speak(self):
        print("Meow")

#a=Animal()
#a.speak()


List=[Dog(), Dog(), Cat(), Dog(), Cat(), Dog()]




for i in range(1,100):
    if random.randint(0,100)<=50:
        List.append(Dog())
    else:
        List.append(Cat())


for i in List:
    i.speak()