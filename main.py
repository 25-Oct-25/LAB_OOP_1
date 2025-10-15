import Panda
pandas = [
    Panda.Panda("Ling-Ling", 5, "Giant Panda", "bamboo forest"),
    Panda.Panda("Hsing-Hsing", 8, "Giant Panda", "bamboo forest"),
    Panda.Panda("Mei Xiang", 3, "Giant Panda", "bamboo forest"),
    Panda.Panda("Tian Tian", 10, "Giant Panda", "bamboo forest")
]


def get_panda_status(pandas_list, panda_name):
    '''
    check name panda is exit then it will call function
    if not return message with no data found
    '''
    for panda in pandas_list:
        if panda.name.lower() == panda_name.lower():
            return panda.get_status()
    return f"No panda found with the name '{panda_name}'."


menu ="""
=== Panda Management Menu ===
1. Add a new Panda
2. Feed a Panda by name
3. Display status of a Panda by name
4. Display all Pandas
5. Exit
Enter Your Choice : """

while True:
    choice = input(menu)

    if choice == "5":
        print("Thank you for managing the pandas! Goodbye!")
        break
    elif choice == "1":
        name = input("Enter the panda's name: ")
        try:
            age = int(input("Enter the panda's age: "))
            type_panda = input("Enter the panda's Type (e.g., Giant Panda): ")
            place = input("Enter the panda's location (e.g., bamboo forest): ")
            new_panda = Panda(name, age, type_panda, place)
            pandas.append(new_panda)
            print(f"Added {name} successfully!")
        except ValueError:
            print("Invalid age! Please enter a number.")
    elif choice in ["2", "3"]:
        panda_name = input("Enter the panda's name: ").lower()
        if choice == "2":  
            for panda in pandas:
                if panda.name.lower() == panda_name:
                    panda.eat_bamboo()
                    break
            else:
                print(f"No panda found with the name '{panda_name}'.")
        elif choice == "3": 
            status = get_panda_status(pandas, panda_name)
            print(status)
    elif choice == "4":
        if not pandas:
            print("No pandas yet! Add one first.")
        else:
            for panda in pandas:
                print(f"Name: {panda.name}, Age: {panda.age}, Type: {panda.Type_panda}, Place: {panda.place}, Bamboo Eaten: {panda.bamboo_eaten:.1f} kg")
    else:
        print("Invalid choice. Try again.")

