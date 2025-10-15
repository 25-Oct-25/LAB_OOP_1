from panda import Panda

def main():
    # Creating instances of the Panda class
    panda1 = Panda("Bao Bao", 5, 120, "Bamboo Forest")
    panda2 = Panda("Lun Lun", 6, 130, "Bamboo Forest")
    panda3 = Panda("Tian Tian", 7, 140, "Bamboo Forest")
    panda4 = Panda("Mei Xiang", 8, 150, "Bamboo Forest")

    # Printing one attribute and calling methods for each panda
    pandas = [panda1, panda2, panda3, panda4]
    
    for panda in pandas:
        print(f"Panda Name: {panda.name}")
        panda.eat("bamboo")
        panda.sleep()

if __name__ == "__main__":
    main()