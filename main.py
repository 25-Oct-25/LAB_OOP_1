from panda_class import Panda
# naming 5 panda and add age, color like Attributes
ella = Panda("Ella", 4, "Black and White", 65)
yamada = Panda("Yamada", 6, "Brown and White", 80)
keven = Panda("Keven", 3, "Black and White", 60)
kamarai = Panda("Kamarai", 5, "Black and Gray", 75)
jessica = Panda("Jessica", 2, "Black and White", 55)

# display information
ella.display_info()
yamada.display_info()
keven.display_info()
kamarai.display_info()
jessica.display_info()

ella.eat("bamboo")
jessica.eat("apple")

ella.display_info()
jessica.display_info()
