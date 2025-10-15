from panda import Panda

p1 = Panda("Bao Bao", 5, "Black & White", "China")
p2 = Panda("Ling Ling", 3, "Brown & White", "Japan")
p3 = Panda("Mimi", 2, "Black & White", "Thailand")
p4 = Panda("Tao Tao", 7, "Gray & White", "Singapore")

pandas = [p1, p2, p3, p4]

for panda in pandas:
    panda.display_info()  # Display all attributes
    panda.eat()           # Call eat method
    panda.sleep()         # Call sleep method
    print("-" * 40)       # Separator between pandas
