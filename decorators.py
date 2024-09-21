"""
Decorators
"""


def add_sprinkles(func):
    def wrapper():
        print("Adding sprinkles 🎉")
        func()

    return wrapper


def add_fudge(func):
    def wrapper():
        print("Adding fudge 🍫")
        func()

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream():
    print("Here is your ice cream 🍨")


get_ice_cream()
