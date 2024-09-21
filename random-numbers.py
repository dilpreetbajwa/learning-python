import random

random_number = random.randint(1, 20)
random_floating_number = random.random()
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

print(random_number)
print(random_floating_number)

random.shuffle(cards)

print(cards)
