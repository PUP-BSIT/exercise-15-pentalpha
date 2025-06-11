from os import system
from pentalpha import bautista, managbanag, banzali, raymundo, espinola

while (True):
    system('cls')
    print("Choose a member: ")
    print("[1] - Bautista")
    print("[2] - Banzali")
    print("[3] - Espinola")
    print("[4] - Managbanag")
    print("[5] - Raymundo")
    print("[0] - Exit")
    menu_choice = input("Enter Choice: ")

    try:
        menu_choice = int(menu_choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        input("Press Any Key to continue...")
        continue

    match (menu_choice):
        case 1:
            pokemon_1 = bautista.Pokemon("Pikachu", "Electric Mouse Pokemon", 
                    "It stores electricity in its cheeks and use it to attack",
                    "Electic")
            pokemon_1.menu()
        case 2:
            driver = banzali.Formula1("Sergio Perez", "Red Bull", "Mexican")
            driver.menu()
        case 3:
            thermo = espinola.SimpleThermostat()
            thermo.menu()
        case 4:
            adventure = managbanag.Adventure("Geralt", "Witcher", 30)
            adventure.menu()
        case 5:
            book_1 = raymundo.Book("1984", "George Orwell", "Dystopian")
            book_1.menu()
        case 0:
            print("Exiting...")
            break
        case _:
            print("Invalid input. Please choose from 0-5.")
        
    input("Press Any Key to continue...")
