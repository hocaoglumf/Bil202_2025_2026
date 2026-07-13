class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Hatalı kısım
        super().speak()
        print(f"{name} barks.")


dog1 = Dog("Karabas", "Kangal")
dog1.speak()