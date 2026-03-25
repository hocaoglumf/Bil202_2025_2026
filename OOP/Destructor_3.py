
class Base:
    def __del__(self):
        print("Base destructor")

class Child(Base):
    def __del__(self):
        print("Child destructor")
        super().__del__()


c = Child()
del c

