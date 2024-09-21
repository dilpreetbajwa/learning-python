"""
Inheritance
"""


class Animal:
    def __init__(
        self,
        name: str,
    ):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print("Woof woof")


class Cat(Animal):
    def meow(self):
        print("Meow")


class Mouse(Animal):
    def squeak(self):
        print("Squeak")


dog = Dog("Rex")
cat = Cat("Whiskers")
mouse = Mouse("Jerry")

print(dog.name)
print(cat.name)
print(mouse.name)

dog.eat()
cat.meow()
mouse.squeak()
