from oop_lab import Panda

#Create 4 instances / objects
giant = Panda("Giant", "China","bamboo", False)
red = Panda("Red", " Eastern Himalayas and China", "bamboo , fruits, acorns, eggs, and insects", True)
qinling = Panda("Qinling","China", "bamboo", True)
melita = Panda("Melita","Japan","bamboo and leaves",False)

#Print 1 attribute value
print(f'{qinling.panda_type} is endangered')

#Calling the method one for each instance
print(giant.information())
print(red.information())
print(qinling.information())
print(melita.information())

#Calling the method two for each instance
print(f'The food of {giant.panda_type} panda :',giant.panda_food())
print(f'The food of {red.panda_type} panda :',red.panda_food())
print(f'The food of {qinling.panda_type} panda :', qinling.panda_food())
print(f'The food of {melita.panda_type} panda :',melita.panda_food())