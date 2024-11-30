import sys
import random

#this is not the same like on the mac

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

    try:
        # Loop to keep asking the user what they want to do
        while True:
            what_to_do = input("What would you like to do at the Koala Lair©? ").strip().lower()

            if what_to_do == "leave the koala lair":
                print("Goodbye from the Koala Lair!")
                sys.exit()  # Terminate the program
            elif what_to_do == "kill koala" or what_to_do == "kill koalas":
                # Print a scolding message in a loop, then exit
                for _ in range(999999999999999999999999999999999):
                    print("You are a bad boyyyyyyyyyyyyy.")
                sys.exit()
            elif what_to_do == "sleep like a koala":
                for _ in range(30):
                    print("koala want to sleep.......................")
                continue  # Go back to the menu after the action
            elif what_to_do == "kiss a kangaroo":
                # This loop will print a ridiculous message multiple times
                for _ in range(99999999999999999999999999999999999999999999999999999999):
                    print("GO AWAY YOU DUMBASS STUPID LIKE YOUR ASS AND BLACK ASS KANGAROO")
                continue  # Go back to the menu after the action
            elif what_to_do == "marry a koala":
                for _ in range(999999):
                    print("Congratulations! You are now married to a koala. Enjoy your eucalyptus-filled life together!")
                continue  # Go back to the menu after the action
            elif what_to_do == "koala trivia":
                print("Welcome to the Koala Trivia Challenge! Let's see how much you know about koalas.")
                print("You will answer 5 questions, and I'll keep track of your score.")

                questions = [
                    ("What do koalas eat?", "eucalyptus"),
                    ("How long do koalas sleep each day?", "18 hours"),
                    ("Are koalas marsupials?", "yes"),
                    ("Where do koalas spend most of their lives?", "trees"),
                    ("How many fingerprints do koalas have?", "one set of fingerprints"),
                ]

                score = 0
                for i, (question, correct_answer) in enumerate(questions, 1):
                    print(f"\nQuestion {i}: {question}")
                    answer = input("Your answer: ").strip().lower()

                    if answer == correct_answer:
                        print("Correct! 🎉")
                        score += 1
                    else:
                        print(f"Oops! The correct answer was '{correct_answer}'. Better luck next time!")

                print("\nThe trivia is over! Here’s your final score:")
                print(f"You got {score}/{len(questions)} questions right.")

                if score == len(questions):
                    print("Amazing! You're a Koala Expert! 🏆")
                elif score >= 3:
                    print("Great job! You're almost a Koala Expert! 😄")
                elif score == 2:
                    print("Not bad! But you can still learn more about our fluffy friends! 🐨")
                else:
                    print("Looks like you need to study koalas a little more! 🧐 Don't give up!")

                continue  # Go back to the menu after the trivia
            elif what_to_do == "koala fact":
                facts = [
                    "Koalas sleep for up to 18 hours a day!",
                    "Koalas are marsupials, not bears!",
                    "Each koala has a unique fingerprint, just like humans!",
                    "Koalas spend most of their lives in trees!",
                    "Koalas eat eucalyptus leaves: Koalas are herbivores and eat mostly eucalyptus leaves. These leaves are toxic to most animals, but koalas have a special digestive system to handle them.",
                    "Koalas are territorial: Koalas are territorial animals. Males have a loud bellowing call that they use to warn other males and mark their territory.",
                    "Koalas' sense of smell helps them choose food: While their sense of sight isn't as developed as some other animals, koalas rely on their sense of smell to select eucalyptus leaves that are best for eating.",
                    "Koalas give birth to tiny babies: Koala babies are called joeys. At birth, they are about the size of a lima bean and spend several months developing in the mother's pouch before emerging.",
                    "Koalas are primarily solitary: Unlike some other animals that live in groups, koalas are typically solitary. They prefer to stay in their own territories unless they are mating.",
                    'Koalas are vulnerable: Due to habitat loss, disease, and other threats, koalas are classified as "vulnerable" in the wild. Conservation efforts are ongoing to protect them and their natural habitat.'
                ]
                print(random.choice(facts))
                continue  # Go back to the menu after showing the fact
            else:
                print("The Koala Lair© cannot do that... yet.")
                continue  # Go back to the menu if the option is not valid

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit()

else:
    print("Goodbye!")
    sys.exit()
