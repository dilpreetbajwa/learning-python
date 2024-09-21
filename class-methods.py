"""
Class methods
"""


class Student:
    count = 0
    total_gpa = 0.0

    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"There are {cls.count} students"

    @classmethod
    def get_average_gpa(cls):
        return f"The average GPA is {cls.total_gpa / cls.count}"


student1 = Student("Alice", 4.0)
student2 = Student("Bob", 3.5)
student3 = Student("Charlie", 3.0)

print(Student.get_count())
print(Student.get_average_gpa())
