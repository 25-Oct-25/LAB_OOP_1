# panda.py
class Panda:
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    # Method 1: Panda eats bamboo
    def eat_bamboo(self):
        print(f"{self.name} is eating bamboo!")

    # Method 2: Panda sleeps
    def sleep(self):
        print(f"{self.name} is sleeping now.")
