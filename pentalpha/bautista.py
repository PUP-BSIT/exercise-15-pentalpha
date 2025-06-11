from os import system

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


    
