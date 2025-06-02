import os
import sys

def main():
    try:
        while True:
            number = input("Hi! What number would you like me to double? ")
            if not number.replace(".", "", 1).isdigit():
                input("Sorry, that's not a number, press Enter to try again.")
                os.system('cls' if os.name == 'nt' else 'clear')
                continue  # loop back and ask again
            number = float(number)
            doubled_number = number * 2
            print(f"The double of {number} is {doubled_number}")
            user_input = input("Hit Enter or type anything and hit Enter to leave. ").lower().strip()
            if user_input == "koala":
                koalalab()
            break  # exit the loop after successful double
    except KeyboardInterrupt:
        print("\nError 4: User quit")
        sys.exit()

def koalaguy():
    name_of_player = input("Hello! What's your name? ")
    reason_of_visit = input(f"Oh! Hi {name_of_player}! What are you here for? ")

def computer():
    print("Please input your username and password.")
    computer_username = input("Username: ")
    computer_pass = input("Password: ")

def koalalab():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Welcome to the Koala Lab©!")
        what_to_do = input("What would you like to do? (type 'help' for options): ").lower().strip()
        if what_to_do == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            helplist = """
Available commands include:

- 'leave' To exit the Koala Lab.
- 'cmd' To go to the Koala Lab computer.
- 'koalaguy' To meet the 'koalaguy'.

        That's it, for now...
"""
            print(helplist)
            input("Press Enter to return to the Koala Lab...")
        elif what_to_do == "leave":
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        elif what_to_do == "cmd":
            computer()
        elif what_to_do == "koalaguy":
            koalaguy()
        else:
            input("That is not an option. Check 'help' for commands.")
            continue

if __name__ == "__main__":
    main()
