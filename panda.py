class Panda:
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight

    def eat(self):
        print(self.name, "is eating bamboo.")

    def sleep(self):
        print(self.name, "is sleeping now.")
