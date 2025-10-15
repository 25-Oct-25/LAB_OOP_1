class Panda:
    
    #initilizer/ constructor
    def __init__(self, name:str, age:int, weight:float, color:str):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color

    #methods
    def information(self):
        information = f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}kg, Color: {self.color}"
        return information
    
    def sleep(self, hours):
        sleep = f"{self.name} slept for {hours} hours"
        return sleep