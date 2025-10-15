# main.py

from LAB_OOP_1.panda import Panda

# create 4 instances/objects
p1 = Panda("Bao", 5, 90.0, "Chengdu Reserve")
p2 = Panda("Ling", 2, 55.5, "Beijing Zoo")
p3 = Panda("Mei", 7, 95.2, "Sichuan Mountains")
p4 = Panda("Tao", 4, 83.0, "Wolong Center")

pandas = [p1, p2, p3, p4]


for p in pandas:
    print(f"\nName attribute → {p.name}")   
    p.eat(kg=3)                              # method 1
    p.sleep(hours=8)                         # method 2

