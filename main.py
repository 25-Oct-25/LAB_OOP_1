from panda import Panda

p1 = Panda("Po", 5, "Female", 100)
p2 = Panda("Ling", 1, "Female", 50)
p3 = Panda("Bao", 12, "Male", 120)
p4 = Panda("Tian", 7, "Male", 90)



# print 1 attribute value, and call the two methods on each instance.
p1.about_panda()
print(f"{p1.name} eats about {p1.bamboo_per_day():.1f} kg of bamboo daily.\n")

p2.about_panda()
print(f"{p2.name} eats about {p2.bamboo_per_day():.1f} kg of bamboo daily.\n")

p3.about_panda()
print(f"{p3.name} eats about {p3.bamboo_per_day():.1f} kg of bamboo daily.\n")

p4.about_panda()
print(f"{p4.name} eats about {p4.bamboo_per_day():.1f} kg of bamboo daily.\n")
