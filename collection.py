"""
Collection

List  = [] ordered and changeable. Duplicates OK
Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
Tuple = () ordered and unchangeable. Duplicates OK. FASTER
"""

# List
fruits = ["apple", "orange", "banana", "coconut"]
fruits.append("watermelon")
fruits.sort()
fruits.reverse()

print(fruits)

# Set
fruits = {"apple", "orange", "banana", "coconut"}
fruits.add("watermelon")
fruits.remove("orange")

print(fruits)

# Tuple
fruits = ("apple", "orange", "banana", "banana", "coconut", "watermelon")

print(fruits.index("apple"))
print(fruits.count("banana"))
