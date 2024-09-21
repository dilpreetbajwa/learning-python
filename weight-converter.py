"""
Weight converter
"""

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")

elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")

else:
    print(f"{unit} is not valid")
