"""
Class variables
"""


class Student:
    class_year = 2024
    number_of_students = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Student.number_of_students += 1


student1 = Student("Alice", 20)
student2 = Student("Bob", 21)
student3 = Student("Charlie", 22)
student4 = Student("David", 23)

print(student1.name)
print(student2.name)

print(Student.class_year)
print(
    f"My graduating class of {Student.class_year} has {Student.number_of_students} students."
)
