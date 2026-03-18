
class Example:

    @classmethod
    def class_method(cls):
        print("Class method:", cls)

    @staticmethod
    def static_method():
        print("Static method")


Example.class_method()
Example.static_method()