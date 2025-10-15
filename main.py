from panda import Panda


def main():
    print("🐼✨ Welcome to the Panda Info Program ✨🐼")
    
    panda1 = Panda("Fu Bao", 4, "Everland Zoo (South Korea)", 98)
    panda2 = Panda("Xiang Xiang", 6, "Ueno Zoo (Japan)", 100)
    panda3 = Panda("Yuan Meng", 7, "Beauval Zoo (France)", 105)
    panda4 = Panda("Bei Bei", 8, "Smithsonian’s National Zoo (USA)", 113)

    pandas = [panda1, panda2, panda3, panda4]

    for panda in pandas:
        print(f"\n🐼 Panda Name: {panda.name}")   # print 1 attribute
        print(f"🏡 Home: {panda.home}")
        print(f"🎂 Age: {panda.age} years")
        print(f"❀❀ Weight: {panda.weight} kg")

        print(panda.eat("fresh bamboo"))             # call the first method
        print(panda.sleep(8))                         # call the second method

    print("\n🌿 Thanks for visiting the panda family! 🌿")

if __name__ == "__main__":
    main()