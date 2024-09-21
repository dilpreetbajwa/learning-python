"""
Object Oriented Programming
"""


class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print("Screech")

    def honk(self):
        print("Beep beep")


car1 = Car("Toyota", 2019, "Red", True)
car2 = Car("Honda", 2020, "Blue", False)

print(car1.model)
print(car2.year)

car1.drive()
car2.stop()
