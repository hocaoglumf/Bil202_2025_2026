class Geek:
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    def __displayDetails(self):
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)

    def accessPrivateFunction(self):
        self.__displayDetails()


obj = Geek("R2J", 1706256, "CSE")

obj.accessPrivateFunction()

print(obj._Geek__name)