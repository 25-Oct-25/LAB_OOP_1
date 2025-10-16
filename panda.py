class Panda:
    def __init__(self, name, age, color, favorite_food):
        self.name = name
        self.age = age
        self.color = color
        self.favorite_food = favorite_food

    def eat(self):
        print(f"{self.name} is eating {self.favorite_food} ")

    def age_years(self):
        print(f"This panda is {self.age} years old")