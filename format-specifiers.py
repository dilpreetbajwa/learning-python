"""
Format specifiers
"""

price1 = 3000.14159
price2 = -987.65
price3 = 1200.34

print("-----------------------")
print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.3f}")
print("-----------------------")
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")
print("-----------------------")
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")
print("-----------------------")
print(f"Price 1 is ${price1:>10}")
print(f"Price 2 is ${price2:>10}")
print(f"Price 3 is ${price3:>10}")
print("-----------------------")
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")
print("-----------------------")
print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }")
print("-----------------------")
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")
print("-----------------------")
print(f"Price 1 is ${price1:+,.3f}")
print(f"Price 2 is ${price2:+,.3f}")
print(f"Price 3 is ${price3:+,.3f}")
print("-----------------------")
