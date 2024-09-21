"""
Membership Operators
"""

# word = "apple"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print("Yes, the letter is in the word.")
# else:
#     print("No, the letter is not in the word.")

# students = {"Alice", "Bob", "Charlie"}

# student = input("Enter a student's name: ")

# if student in students:
#     print(f"{student} is enrolled in the class.")
# else:
#     print(f"{student} is not enrolled in the class.")

grades = {"Alice": "A", "Bob": "B+", "Charlie": "A+"}

student = input("Enter a student's name: ")

if student in grades:
    print(f"{student} has a grade of {grades[student]}.")
else:
    print(f"{student} does not have a grade.")
