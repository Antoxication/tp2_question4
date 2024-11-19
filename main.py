from concepts.polymorphism import test_polymorphism
from concepts.overloading import test_overloading
from concepts.overriding import test_overriding
from concepts.generics import test_generics
from concepts.modularity import test_modularity

if __name__ == "__main__":
    print("Polymorphism:", test_polymorphism())
    print("Overloading:", test_overloading())
    print("Overriding:", test_overriding())
    print("Generics:", test_generics())
    print("Modularity:", test_modularity())
