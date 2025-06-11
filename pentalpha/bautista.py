from os import system

EXIT_OPTION = 0
UNSET_OPTION = -1

class Pokemon:
    def __init__(self, name, nickname, description, type_1="None", 
                type_2="None"):
        """ Constructor for Pokemon class """
        self.name = name
        self.nickname = nickname
        self.description = description
        self.type_1 = type_1
        self.type_2 = type_2

    def inspect(self):
        """ Prints the details of the Pokemon """
        print(f"\nYou encountered a {self.name}")
        print(f"Primary Type: {self.type_1}")
        print(f"Secondary Type: {self.type_2}")
        print(f"\n{self.nickname}")
        print(f"{self.description}")

    def change_name(self):
        """ Changes the name of the Pokemon """
        new_name = input("Enter Pokemon Name: ")

        if not new_name.isalpha() or len(new_name) < 4:
            print("Please enter a valid name!")
            print("Name must be 4 characters or more!")
            return
        
        self.name = new_name

    def change_types(self):
        """ Changes the two types of the Pokemon """
        print("Leave second type blank for single type Pokemon")
        new_type_1 = input("Enter New Primary Type: ")

        if (new_type_1 == ""):
            print("Primary type cannot be empty!")
            return

        new_type_2 = input("Enter New Secondary Type: ")

        # Secondary type can be empty
        if (new_type_2 == ""):
            new_type_2 = "None"

        if (not new_type_1.isalpha()) or (not new_type_2.isalpha()):
            print("Please enter valid type! It must be alphabetic")
            return
        
        self.type_1 = new_type_1
        self.type_2 = new_type_2

    def listen(self):
        """ Prints the cry of the Pokemon """
        cry = self.name[0:4]
        print(f"{cry} {cry}")

    def change_pokedex(self):
        """ Changes the nickname and description of the Pokemon """
        new_nickname = input("Enter new nickname: ")
        new_description = input("Enter new description: ")

        if (not new_nickname.isalpha()) or (not new_description.isalpha()):
            print("Enter a valid nickname and description!")
            print("Description must be alphabetic")
            return
        
        self.nickname = new_nickname
        self.description = new_description

    def menu(self):
        """ Handles the menu and processes user choices """
        choice = UNSET_OPTION
        while(choice != EXIT_OPTION):
            choice = self.display_menu_choice()
            self.process_choice(choice)
           
    def display_menu_choice(self):
        """ Displays the menu and returns the user's choice """
        system('cls')
        print("Pokemon Creator ")
        print("[1] - Inspect Pokemon")
        print("[2] - Change Name")
        print("[3] - Change Typing")
        print("[4] - Listen to Pokemon Cry")
        print("[5] - Change Pokedex Entry")
        print("[0] - Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number!")
            return UNSET_OPTION
        
        return choice 
    
    def process_choice(self, choice):
        """ Processes the user's choice based from the menu """
        match choice:
            case 1:
                self.inspect()
            case 2:
                self.change_name()
            case 3:
                self.change_types()
            case 4:
                self.listen()
            case 5:
                self.change_pokedex()
            case 0:
                print("Exiting...")
                return EXIT_OPTION
            case _:
                print("Invalid choice: Please choose from 0-5")
        
        input("Press Any Key to continue...")

        


    
