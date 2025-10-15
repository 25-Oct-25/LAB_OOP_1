import random
class Panda:

    def __init__(self,name:str,age:int,Type_panda:str,place:str):
        self.name =name
        self.Type_panda=Type_panda
        self.age=age
        self.place=place
        self.bamboo_eaten = 0.0 


    

    def get_status(self):
        status = "DONE" if self.bamboo_eaten > 20 else "NOT DONE"
        return f"Status - Name: {self.name}, Age: {self.age}, Type: {self.Type_panda}, Bamboo Eaten: {self.bamboo_eaten:.1f} kg, Place: {self.place}, Task: {status}"
    
 
    def eat_bamboo(self):
        amount = random.uniform(5, 10)
        self.bamboo_eaten += amount
        print(f"{self.name} ate {amount:.1f} kg of bamboo! Total: {self.bamboo_eaten:.1f} kg.")
