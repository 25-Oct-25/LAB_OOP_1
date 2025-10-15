

class Panda:
    def __init__(self,name,age,home,weight) -> None:
        self.name = name
        self.age = age
        self.home = home
        self.weight = weight

    def eat(self, food):
        return f"{self.name} is happily eating {food} 🐼🎋🎋"
    
    def sleep(self, hours):
        return f"💤{self.name} curls up and sleeps peacefully for {hours} hours... 😴💤"
