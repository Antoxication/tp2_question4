class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

def test_overriding():
    child = Child()
    return child.greet()
