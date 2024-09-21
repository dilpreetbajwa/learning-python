"""
Iterables
"""

numbers: list[int] = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)

fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)

name = "John Doe"

for character in name:
    print(character)

dictionary = {"name": "John", "age": 30, "city": "New York"}

for key, value in dictionary.items():
    print(f"{key}: {value}")
