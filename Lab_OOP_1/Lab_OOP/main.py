# main.py
from panda import Panda  

panda1 = Panda("Bao Bao", 3, "Black & White", 90)
panda2 = Panda("Ling Ling", 5, "Black & White", 100)
panda3 = Panda("Mei Xiang", 7, "Black & White", 95)
panda4 = Panda("Tian Tian", 4, "Black & White", 92)

# List of all pandas
pandas = [panda1, panda2, panda3, panda4]

# Loop through each panda
for panda in pandas:
    print(f"Name: {panda.name}")  
    panda.eat_bamboo() 
    panda.sleep()      
    print()  
