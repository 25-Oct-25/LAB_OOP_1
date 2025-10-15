from panda import Panda

# Create 4 pandas with different traits
panda1 = Panda("Giant Panda ", "Bamboo 🎋", "Happy 😄", 100 )
panda2 = Panda("Red Panda ", "Apples 🍎", "Sleepy 🌙 ", 80)
panda3 = Panda("Giant Panda ", "Carrots 🥕", "Playful 😎", 90)
panda4 = Panda("Red Panda ", "Leaves 🥬", "Curious 🧐", 75)

pandas = [panda1, panda2, panda3, panda4]

for panda in pandas:
    print(f"\nSpecies: {panda.species} 🐼")         
    print(f"Weight: {panda.weight} kg")         
    panda.eat()                                  
    panda.show_mood()                            
