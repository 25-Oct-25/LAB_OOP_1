import classes
pandas=[
classes.Panda("Jake", 140, 6,"white"),
classes.Panda("Paul", 130, 3,"black"),
classes.Panda("Mike", 176, 10,"black"),
classes.Panda("Tyron",145,9,"white"),
]

for panda in pandas:
    print(f"{panda.name} is {panda.age} years old")
    print(panda.make_sound())
    print(panda.feed())



