from os import system

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
            # TODO: (Bautista) Instance class from bautista module
            pass
        case 2:
            # TODO: (Banzali) Instance class from banzali module
            pass
        case 3:
            # TODO: (Espinola) Instance class from espinola module
            pass
        case 4:
            # TODO: (Managbanag) Instance class from managbanag module
            pass
        case 5:
            # TODO: (Raymundo) Instance class from raymundo module
            pass
        case 0:
            print("Exiting...")
            break
        case _:
            print("Invalid input. Please choose from 0-5.")
        
    input("Press Any Key to continue...")
