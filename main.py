from panda import Panda

# 4 instances/objects of the class Panda

            # type, age, color, weight
p1=Panda("Giant Panda", 2, "Black & White", 60)
p2=Panda("Red Panda", 5, "Brown", 75)
p3=Panda("Giant Panda", 9, "Black & White", 90)
p4=Panda("Red Panda", 1, "Gray", 55)


# print 1 attribute value
print(f"type 1 is a {p1.type}")
print(f"type 2 is a {p2.type}")


# call the two methods on each instance
print("\nPandas Info:")
for panda in [p1, p2, p3, p4]:
    panda.personality()
    panda.age_stage()
    print("-" * 30)
