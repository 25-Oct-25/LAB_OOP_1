
#Create a class
class Panda:

    #Create 4 attributes
    def __init__(self, panad_type:str, live:str, food:str, endangered:bool):
        self.panda_type = panad_type
        self.live = live
        self.food = food
        self.endangered = endangered
    
    #Create method one
    def information(self) -> str:
        info = f'- The panda type : {self.panda_type} \n - The panda place : {self.live} \n - The panda food : {self.food} \n - Endangered : {self.endangered}'
        return info

    #Create method two
    def panda_food(self)->str:
        #*pab in korean means food
        pab = f'{self.food}'
        return pab