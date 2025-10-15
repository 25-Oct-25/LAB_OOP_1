
class Panda:
    def __init__(self, name, age, color, location):
        """Initialize panda attributes"""
        self.name = name
        self.age = age
        self.color = color
        self.location = location

    def eat(self):
        """Simulate the panda eating"""
        print(f"{self.name} is eating bamboo! ")

    def sleep(self):
        """Simulate the panda sleeping"""
        print(f"{self.name} is sleeping at {self.location} ")
    
    def display_info(self):
        """Display all information about the panda"""
        print(f"--- Panda Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")
        print(f"Location: {self.location}")
