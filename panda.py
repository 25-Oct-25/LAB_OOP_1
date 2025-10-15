class Panda:
    def __init__(self, type, age, color, weight):
        self.type=type
        self.age=age 
        self.color=color
        self.weight=weight

   
    def personality(self):
        if self.type.lower() == "giant panda":
            print(f"{self.type} is friendly")
        else:
            print(f"{self.type} is a bit wild but still adorable")

    def age_stage(self):
        if self.age < 3:
            print(f"{self.age} years old - baby panda")
        elif self.age < 8:
            print(f"{self.age} years old - young panda")
        else:
            print(f"{self.age} years old - old wise panda")


