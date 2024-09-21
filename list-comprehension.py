"""
List comprehension
"""

doubles = [2 * n for n in range(10)]
print(doubles)

fruits = ["apple", "banana", "cherry"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1, -2, 3, -4, 5, -6]
positive_numbers = [n for n in numbers if n > 0]
negative_numbers = [n for n in numbers if n < 0]
print(positive_numbers)
print(negative_numbers)
