from panda import Panda

p1 = Panda("Luna", 3, "black and white", "bamboo")
p2 = Panda("Bao Bao", 5, "white and gray", "apples")
p3 = Panda("Mei Mei", 2, "black and white", "carrots")
p4 = Panda("Po", 4, "white and black", "bamboo shoots")

print("Panda Name:", p1.name)
print()

p1.eat()
p1.age_years()
print()

p2.eat()
p2.age_years()
print()

p3.eat()
p3.age_years()
print()

p4.eat()
p4.age_years()
