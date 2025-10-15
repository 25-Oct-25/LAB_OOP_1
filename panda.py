# panda.py
class Panda:
    def __init__(self, species, favorite_food, mood, weight):
        self.species = species             # Type of panda
        self.favorite_food = favorite_food # Favorite food
        self.mood = mood                   # Current mood
        self.weight = weight               # Weight in kg

    #  Panda eats
    def eat(self):
        print(f"The {self.species} panda is eating {self.favorite_food} ")

    #  Show current mood
    def show_mood(self):
        print(f"The {self.species} panda is currently {self.mood} ")
