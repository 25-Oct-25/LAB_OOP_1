from panda import Panda

#creating instances/ objects
panda1 = Panda("Lingling", 3, 70, "Black & White")
panda2 = Panda("MeiMei", 5, 88, "White with Black Spots")
panda3 = Panda("TaoTao", 2, 60, "Light Brown & White")
panda4 = Panda("BaoBao", 7, 95, "Classic Black & White")

#calling a method
print(panda1.information())
print(panda1.sleep(10) , "\n")

print(panda2.information())
print(panda2.sleep(13), "\n")

print(panda3.information())
print(panda3.sleep(15), "\n")

print(panda4.information())
print(panda4.sleep(8), "\n")

#accessing an attribute/peroperty
print(f"panda1 its name is {panda1.name}")
print(f"panda2 its age is {panda2.age}")
print(f"panda3 its weight is {panda3.weight}")
print(f"panda4 its weight is {panda4.color}")
