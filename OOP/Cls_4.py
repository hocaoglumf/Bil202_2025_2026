class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)


# Kullanım
t = Temperature.from_fahrenheit(68)

print(t.celsius)  # 20.0