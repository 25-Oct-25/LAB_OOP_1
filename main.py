# Min
from panda import Panda

panda1 = Panda("Panda", 5, "Black & White", 90)
panda2 = Panda("Panda2", 7, "Black & White", 100)
panda3 = Panda("Panda3", 4, "Black & White", 85)
panda4 = Panda("Panda24", 6, "Black & White", 95)

pandas = [panda1, panda2, panda3, panda4]

for panda in pandas:
    print(f"Panda Name: {panda.name}")
    panda.eat()
    panda.sleep()
    print("----------------------")
