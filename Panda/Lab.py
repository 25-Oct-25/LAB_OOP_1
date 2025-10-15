class Panda:
    def __init__(self, name, species, home, age):
        
        self.name=name
        self.species=species
        self.home=home
        self.age=age

    def meet_me(self):
        intro= f"Hello my name is {self.name}, I am a {self.species} Panda, and I am {self.age} years old."
        return intro

    def live(self):
        my_home= f"I live in {self.home}\n"
        return my_home