"""
Args and Kwargs
"""


def add(*args: float) -> float:
    sum: float = 0

    for arg in args:
        sum += arg

    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def print_address(**kwargs: str):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(
    name="John", address="123 Main St", city="New York", state="NY", zip="10001"
)
