import random
from os import system

EXIT_OPTION = 0
UNSET_OPTION = -1

class Formula1:
    def __init__(self, name, team, nationality, speed=80, mode="Normal"):
        """ Constructor for Formula 1 class """
        self.name = name
        self.team = team
        self.nationality = nationality
        self.speed = speed
        self.mode = mode
    
    def profile(self):
        """ Prints the details of Formula 1 Drivers """
        print("====================================")
        print("🏁       Formula 1 Drivers       🏁")
        print("====================================")
        print(f"Name          : {self.name}")
        print(f"Team          : {self.team}")
        print(f"Nationality   : {self.nationality}")
        print(f"Current speed : {self.speed}")
        print(f"Mode          : {self.mode}")
        
    def accelerate(self):
        """ Changes the speed of the car """
        increment = [30, 40, 50]
        random_increment = random.choice(increment)
        self.speed += random_increment
        
        print(f"\n{self.name} accelerated by {random_increment} km/h! "
                + f"Current speed: {self.speed} km/h")
        
    def change_mode(self):
        """ Changes the driving mode """
        print("====================================")
        print("🏁      Select Driving Mode      🏁")
        print("====================================")
        print("[1] Normal")
        print("[2] Attack Mode")
        print("[3] Eco Mode")

        choice = int(input("Choose a mode: "))
        
        match choice:
            case '1':
                self.mode = "Normal"
                print(f"\nMode changed to {self.mode}.")
            case '2':
                self.mode = "Attack Mode"
                print(f"\nMode changed to {self.mode}.")
            case '3':
                self.mode = "Eco Mode"
                print(f"\nMode changed to {self.mode}.")
            case _:
                print("Invalid mode selected.")
    
    def pit_stop(self):
        """ Resets the speed """
        print("\nYou entered the pit stop...")
        self.speed = 0
        print("Tires changed. Fuel topped. Speed reset to 0 km/h.")
        print("Goodluck mate! - Gabrielle")

    def rename_driver(self, speed=80, mode="Normal"):
        """ Changes the details of the driver """
        print("====================================")
        print("🏁          New Driver           🏁")
        print("====================================")
        new_name = input("Driver name: ")
        new_team = input("Team: ")
        new_nationality = input("Nationality: ")

        if not (new_name.replace(" ", "").isalpha()
                and new_team.replace(" ", "").isalpha()
                and new_nationality.isalpha):
            print("Please enter a valid name and team.")
            return
        
        self.name = new_name
        self.team = new_team
        self.nationality = new_nationality
        self.speed = speed
        self.mode = mode

    def menu(self):
        """ Handles the menu and processes user choices """
        choice = UNSET_OPTION
        while(choice != EXIT_OPTION):
            choice = self.display_menu()
            self.user_menu(choice)

    def display_menu(self):
        """ Display the menu and return's user choice"""
        system("cls")
        print("====================================")
        print("🏁      Formula 1 Simulator      🏁")
        print("====================================")
        print("[1] View Profile")
        print("[2] Accelerate")
        print("[3] Change Driving Mode")
        print("[4] Pit Stop")
        print("[5] New Driver")
        print("[0] Exit to Main Menu")

        try:
            choice = int(input("Select option (0-5): "))
        except ValueError:
            print("Please enter a valid number!")
            return UNSET_OPTION

        return choice 

    def user_menu(self, choice):
        """ Enters user choice based from the menu """
        match choice:
            case 1:
                system("cls")
                self.profile()
            case 2:
                self.accelerate()
            case 3:
                system("cls")
                self.change_mode()
            case 4:
                self.pit_stop()
            case 5:
                system("cls")
                self.rename_driver()
            case 0:
                print("Back to the menu...")
                return EXIT_OPTION
            case _:
                print("Invalid option. Please choose from 0-5.")

        input("\nPress Enter to continue...")