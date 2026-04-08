
class Test:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

def func():
    t = Test()

func()
func()

print("")

t = Test()
t = Test()
