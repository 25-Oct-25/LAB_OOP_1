# panda.py

class Panda:
    def __init__(self, name: str, age: int, weight: float, habitat: str):
        # 4 attributes
        self.name = name
        self.age = age
        self.weight = weight
        self.habitat = habitat

    # method 1
    def eat(self, kg: float):
        """Increase weight a little after eating bamboo."""
        self.weight += kg * 0.1
        print(f"{self.name} eats {kg} kg of bamboo → weight now {self.weight:.1f} kg")

    # method 2
    def sleep(self, hours: int):
        """Print a simple sleeping message."""
        print(f"{self.name} sleeps for {hours} hours in {self.habitat}.")

