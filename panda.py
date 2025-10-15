class Panda:
    def __init__(self, name, age, weight, habitat):
        self.name = name        # Name of the panda
        self.age = age          # Age of the panda
        self.weight = weight    # Weight of the panda in kg
        self.habitat = habitat  # Habitat of the panda

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")