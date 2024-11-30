import sys

# This program doubles the number you give it.
number_to_double = input("What number should I double? ")

# Convert the input to a number
try:
    number_to_double = float(number_to_double)
    answer = number_to_double * 2
    print(f"The answer is: {answer}")
except ValueError:
    print("Please enter a valid number.")

# Subtle secret feature
user_input = input("Press Enter to close the program, or type anything and hit Enter: ").strip().lower()

if user_input == "koala":
    print("\nWelcome to the Koala Lair©!")
    what_to_do = input("What would you like to do at the Koala Lair©? ").strip().lower()
    
    if what_to_do == "leave the koala lair":
        print("Goodbye from the Koala Lair!")
        sys.exit()  # Terminate the program
    elif what_to_do == "kill koala" or what_to_do == "kill koalas":
        # Print a scolding message in a loop, then exit
        for _ in range(5):  # Limit the loop to 5 messages to avoid overloading the user
            print("You are a bad boyyyyyyyyyyyyy.")
        sys.exit()
    elif what_to_do == "sleep like a koala":
        for _ in range(30):
        print("koala want to sleep.......................")
        sys.exit()
    else:
        print("The Koala Lair©, can not do that... yet.")
else:
    print("Goodbye!")
    sys.exit()