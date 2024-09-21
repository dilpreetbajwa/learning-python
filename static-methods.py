"""
Static methods
"""


class Employee:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"

    @staticmethod
    def is_valid_position(position):
        return position in ["Manager", "Developer", "Designer"]


employee1 = Employee("John", "Manager")

print(Employee.is_valid_position("Manager"))
print(Employee.is_valid_position("Pizza"))

print(employee1.get_info())
