from os import system

UNSET_OPTION = -1
EXIT_OPTION = 0

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def show_info(self):
        """Show the current book details."""
        print("\nBook Info:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        input("\nPress Any Key to continue...")

    def change_title(self):
        """Allow the user to change the book's title."""
        new_title = input("Enter new title: ")

        if new_title.strip() and new_title.replace(" ", "").isalpha():
            self.title = new_title
            print(f"Title changed to '{self.title}'.")
        else:
            print("Invalid title! Please enter alphabetic characters only.")
        
        input("\nPress Any Key to continue...")

    def change_author(self):
        """Allow the user to change the book's author."""
        new_author = input("Enter new author: ")

        if new_author.strip() and new_author.replace(" ", "").isalpha():
            self.author = new_author
            print(f"Author changed to '{self.author}'.")
        else:
            print("Invalid author! Please enter alphabetic characters only.")
        
        input("\nPress Any Key to continue...")

    def change_genre(self):
        """Allow the user to change the book's genre."""
        new_genre = input("Enter new genre: ")

        if new_genre.strip() and new_genre.replace(" ", "").isalpha():
            self.genre = new_genre
            print(f"Genre changed to '{self.genre}'.")
        else:
            print("Invalid genre! Please enter alphabetic characters only.")
        
        input("\nPress Any Key to continue...")

    def summary(self):
        """Show a short summary of the book."""
        print(f"'{self.title}' is a {self.genre} book",
                "written by {self.author}.")
        input("\nPress Any Key to continue...")

    def menu(self):
        """Handles the menu and processes user choices."""
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.display_menu_choice()

            if choice == EXIT_OPTION:
                print("Exiting Book Manager...")
                break
            
            self.process_choice(choice)

    def display_menu_choice(self):
        """Displays the menu and returns the user's choice."""
        system('cls')
        print("=== Book Manager ===")
        print("[1] Show Book Info")
        print("[2] Change Title")
        print("[3] Change Author")
        print("[4] Change Genre")
        print("[5] Show Book Summary")
        print("[0] Exit")
        print("====================")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number!")
            input("Press Enter to continue...")
            return UNSET_OPTION

        return choice

    def process_choice(self, choice):
        """Processes the user's choice from the menu."""
        match choice:
            case 1:
                self.show_info()
            case 2:
                self.change_title()
            case 3:
                self.change_author()
            case 4:
                self.change_genre()
            case 5:
                self.summary()
            case _:
                print("Invalid choice. Please choose from 0-5.")