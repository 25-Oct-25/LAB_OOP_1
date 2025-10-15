from panda_class import Panda

p1 = Panda("Lulu", 5, "Black & White", 90)
p2 = Panda("Bao", 3, "Black & White", 80)
p3 = Panda("Tian", 4, "Gray & White", 85)
p4 = Panda("Mimi", 6, "Brown", 95)

for panda in [p1, p2, p3, p4]:
    print(f"{panda.name}'s color is {panda.color}")
    panda.eat()
    panda.sleep()
    print("-" * 20)