# panda_class.py
class Panda:
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    def display_info(self):
        print(f"Panda Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Color: {self.color}")#Attributes
        print(f"Weight: {self.weight} kg")#Attributes
        print("-" * 20)

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

