class Panda:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."
