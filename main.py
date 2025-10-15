from panda import Panda

p1 = Panda("Gobran", 5, "Black and White", 90)
p2 = Panda("Muid", 7, "Black", 100)
p3 = Panda("Marai", 4, "Black and White", 88)
p4 = Panda("Jasem", 6, "white", 105)

print(f"Name: {p1.name}  Age: {str(p1.age)}  Color: {p1.color}  Weight: {str(p1.weight)}")
print(f"Name: {p2.name}  Age: {str(p2.age)}  Color: {p2.color}  Weight: {str(p2.weight)}")
print(f"Name: {p3.name}  Age: {str(p3.age)}  Color: {p3.color}  Weight: {str(p3.weight)}")
print(f"Name: {p4.name}  Age: {str(p4.age)}  Color: {p4.color}  Weight: {str(p4.weight)}")

for panda in [p1, p2, p3, p4]:
    panda.eat()
    panda.sleep()
