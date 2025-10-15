
class Panda:
    def __init__ (self, name, weight, age, color):
        self.name=name
        self.weight=weight
        self.age=age
        self.color=color

    def get_color(self):
        return self.color
    def get_age(self):
        return self.age
    def make_sound(self):
        return ("panda sound?")
    def feed(self):
        return( f"{self.name} is eating")