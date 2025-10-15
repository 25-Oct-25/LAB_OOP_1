class Panda:
    #constructor
    def __init__(self, name: str, age: int, weight: float, species: str):
        self.name = name
        self.age = age
        self.weight = weight
        self.species = species

    def pandaSpecies(self):
        print(f"{self.name} is a {self.species}")

    def sleepHours(self):
        if self.age <= 2:
            print(f"{self.name} is only {self.age} years old, so it sleeps around 11 - 16 hours!")
        elif self.age <= 12:
            print(f"{self.name} is {self.age} years old, so it sleeps around 9 - 13 hours a day.")
        else:
            print(f"{self.name} is {self.age} years old, so it needs less sleep, about 8 hours daily.")

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.weight:.1f} kg, and it is a {self.species}"