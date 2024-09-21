"""
Default arguments
"""

# def net_price(price: float, discount: float = 0, tax: float = 0.05) -> float:
#     return price * (1 - discount) * (1 + tax)


# print(net_price(500, 0.1))

# import time


# def count(start: int, end: int):
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("Done!")


# count(1, 5)


def hello(greeting: str, title: str, first: str, last: str):
    print(f"{greeting} {title} {first} {last}")


hello(title="Mr", first="John", last="Doe", greeting="Hello")
