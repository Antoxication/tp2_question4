class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def test_polymorphism():
    dog = Dog()
    cat = Cat()
    return [dog.speak(), cat.speak()]
