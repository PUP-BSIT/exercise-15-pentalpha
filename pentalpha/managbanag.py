from faker import Faker
from os import system

EXIT_OPTION = 0
UNSET_OPTION = -1

class Adventure:
    def __init__(self, first_name, last_name, age):
        """Initialize Adventure instance with user info."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fake = Faker()

    def tell_riddle(self):
        """Present a random riddle and check the answer."""
        riddles = [(
                "What has keys but can't open locks?",
                "piano"
            ),
            (
                "I speak without a mouth and hear without ears."
                " What am I?",
                "echo"
            ),
            (
                "What can travel around the world while staying"
                " in a corner?",
                "stamp"
            ),]
        question, answer = self.fake.random_element(riddles)
        print(f"\nRiddle: {question}")
        response = input("Answer: ").strip().lower()

        if response == answer:
            print("Correct!")
        else:
            print("Incorrect!")
            print("Better luck next time!")
            print(f"The answer was '{answer}'.")

        input("\nPress any key to proceed...")

    def generate_companion(self):
        """Create a companion profile using Faker."""
        code_name = self.fake.color_name() + " Ghost"
        hometown = self.fake.city()
        skill_list = [
            "Invisibility",
            "Telepathy",
            "Hacking",
            "Martial Arts",
            "Sniping"
        ]
        skills = self.fake.random_elements(elements=skill_list)
        safe_house = self.fake.address()

        print("\n|--Companion Profile--|")
        print(f"Code Name: {code_name}")
        print(f"Hometown: {hometown}")
        print(f"Skills: {', '.join(skills)}")
        print(f"Safe House: {safe_house}")
        input("\nPress any key to proceed...")

    def tavern_tale(self):
        """Tell a random adventure-themed joke."""
        jokes = [
            ("Why do dragons always sleep facing east?",
             "Because they want to keep one eye on the sunrise!"),
            ("What do elves put on their toast?",
             "Fairy jam!"),
            ("Why did the rogue hide under the bed?",
             "He heard the floorboard spirits whisper!"),
        ]
        setup, punch = self.fake.random_element(jokes)
        print("\n|--Tales from the Tavern--|")
        print(setup)
        input("Press any key for the punchline...")
        print(punch)
        input("\nPress any key to proceed...")

    def your_quest(self):
        """Offer a one-line adventure prompt."""
        location = self.fake.city()
        creature = self.fake.random_element([
            "dragon", 
            "goblin", 
            "phoenix", 
            "kraken", 
            "wizard"
        ])
        item = self.fake.random_element([
            "ancient amulet", "mystic sword",
            "enchanted map", "lost scroll", "crystal orb"
        ])
        print(f"\nExplore {location} to retrieve a {item}")
        print(f"guarded by a {creature}.")
        input("\nPress any key to proceed...")

    def generate_npc(self):
        """Generate a random NPC with name, role, and backstory."""
        name = self.fake.name()
        role = self.fake.job()
        trait = self.fake.catch_phrase()
        town = self.fake.city()
        print("\n|--NPC Profile--|")
        print(f"Name: {name}")
        print(f"Role: {role}")
        print(f"Trait: {trait}")
        print(f"From: {town}")
        input("\nPress any key to proceed...")

    def menu(self):
        """Handles the menu and processes user choices"""
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.display_menu_choice()
            self.process_choice(choice)

    def display_menu_choice(self):
        """Displays the menu and returns the user's choice"""
        system("cls")
        print("\n-- Adventure Menu  --")
        print("[1] - Solve Riddle")
        print("[2] - Generate Companion")
        print("[3] - Tales from the Tavern")
        print("[4] - Your Quest")
        print("[5] - Generate NPC")
        print("[0] - Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a valid number!")
            return UNSET_OPTION

        return choice

    def process_choice(self, choice):
        """Processes the user's choice based from the menu"""
        match choice:
            case 1:
                self.tell_riddle()
            case 2:
                self.generate_companion()
            case 3:
                self.tavern_tale()
            case 4:
                self.your_quest()
            case 5:
                self.generate_npc()
            case 0:
                print("Exiting...")
                return EXIT_OPTION
            case _:
                print("Invalid choice: Please choose from 0-5")