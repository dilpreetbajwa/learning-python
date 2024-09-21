"""
Functions
"""


def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")


happy_birthday("John", 20)
happy_birthday("Tom", 19)
happy_birthday("Peter", 21)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}!")
    print(f"Your invoice amount is {amount} and is due on {due_date}")


display_invoice("John", 100, "2021-12-31")
display_invoice("Tom", 200, "2021-12-31")


# Return a value to the caller
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print(add(10, 20))
print(subtract(20, 10))
print(multiply(10, 20))
print(divide(20, 10))
