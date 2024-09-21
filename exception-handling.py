"""
Exception handling
"""

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You cannot divide by 0")
except ValueError:
    print("You must enter a number")
except Exception as e:
    print("Something went wrong")
    print(e)
finally:
    print("This will always run")
