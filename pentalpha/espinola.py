from os import system

UNSET_OPTION = -1
EXIT_OPTION = 0

class SimpleThermostat:
    def __init__(self, current_temp=20, is_on=True, mode="heat"):
        self.current_temp = current_temp
        self.is_on = is_on
        self.mode = mode

    def set_temp(self, new_temp):
        """Set target temperature"""
        try:
            new_temp= float(new_temp)
        except ValueError:
            print("Please enter a valid number.")
            return 

        if 10 <= new_temp <= 30:
            self.current_temp = new_temp
            print(f"Temperature set to {new_temp}°C")
        else:
            print("Temperature must be between 10°C and 30°C")

    def toggle_power(self):
        """Turn thermostat on/off"""
        self.is_on = not self.is_on
        state = "ON" if self.is_on else "OFF"
        print(f"Power {state}")

    def change_mode(self, new_mode):
        """Switch between heat/cool/off"""
        new_mode = new_mode.lower()
        
        if new_mode in ["heat", "cool", "off"]:
            self.mode = new_mode
            print(f"Mode set to {new_mode}")
        else:
            print("Invalid mode (choose: heat/cool/off)")

    def status(self):
        """Display current settings"""
        print("\nSTATUS:\n")
        print(f"Temperature: {self.current_temp}°C\n")
        print(f"Power: {'ON' if self.is_on else 'OFF'}")
        print(f"Mode: {self.mode.upper()}")
    
    def show_fahrenheit(self):
        """Displays the current temperature in Fahrenheit"""
        fahrenheit = (self.current_temp * 9/5) + 32
        print(f"Current Temperature: {fahrenheit:.1f}°F")

    def menu(self):
        """Handles the menu and processes user choices"""
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.display_menu_choice()
            self.process_choice(choice)

    def display_menu_choice(self):
        """Displays the menu and returns the user's choice"""
        system('cls')
        print("=== SIMPLE THERMOSTAT ===")
        print("[1] - Set Temperature")
        print("[2] - Toggle Power")
        print("[3] - Change Mode")
        print("[4] - Show Status")
        print("[5] - Show Temperature in Fahrenheit")
        print("[0] - Exit")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a valid number!")
            return UNSET_OPTION

        return choice

    def process_choice(self, choice):
        """Processes the user's choice from the menu"""
        match choice:
            case 1:
                temp = input("Enter temperature (10-30°C): ")
                self.set_temp(temp)
            case 2:
                self.toggle_power()
            case 3:
                mode = input("Enter mode (heat/cool/off): ")
                self.change_mode(mode)
            case 4:
                self.status()
            case 5:
                self.show_fahrenheit()
            case 0:
                print("Goodbye!")
                return EXIT_OPTION
            case _:
                print("Invalid choice: Please choose from 0-5")

        input("Press any key to continue...")




