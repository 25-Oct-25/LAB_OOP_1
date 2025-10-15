class Panda:
    def __init__(self,name:str,age:int,gender:str,weight:float):
        self.name = name    
        self.age = age          
        self.gender = gender     
        self.weight = weight 

    def about_panda(self):
        print(f"Panda {self.name} is {self.age} years old and the gender is {self.gender}, with a weight of {self.weight} kg.")


    def bamboo_per_day(self):
        """Calculate how much bamboo the panda eats daily (30% of body weight)."""
        return self.weight * 0.3


