import random

# ---------------------------------------------------------------
# Tool 1: Number Guessing Game
# The computer picks a secret number from 1 to 10. The player keeps
# guessing, getting "too high" or "too low" hints, until correct.
# ---------------------------------------------------------------
def guessing_game():
    secret = random.randint(1, 10)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 10.")

    while True:
        guess_text = input("Your guess: ").strip()
        if not guess_text.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess_text)
        attempts += 1

        if guess < secret:
            print("Too low, try again!")
        elif guess > secret:
            print("Too high, try again!")
        else:
            print(f"Correct! You got it in {attempts} attempt(s). Well done!")
            break


# ---------------------------------------------------------------
# Tool 2: To-Do List
# Keeps a list of tasks that changes while the program runs. The user
# can add a task, view all tasks, or mark one done (removing it).
# ---------------------------------------------------------------
def todo_list():
    tasks = []
    print("\n--- To-Do List ---")

    while True:
        action = input("add / done / show / back: ").strip().lower()

        if action == "add":
            task = input("New task: ").strip()
            if task == "":
                print("A task can't be empty.")
            else:
                tasks.append(task)
                print(f"Added '{task}'. You now have {len(tasks)} task(s).")

        elif action == "done":
            task = input("Which task did you finish? ").strip()
            if task in tasks:
                tasks.remove(task)
                print(f"Nice work! '{task}' is complete.")
            else:
                print("That task is not on your list.")

        elif action == "show":
            if len(tasks) == 0:
                print("Your to-do list is empty. Enjoy the free time!")
            else:
                number = 1
                for task in tasks:
                    print(f"{number}. {task}")
                    number += 1

        elif action == "back":
            print("Returning to the main menu...")
            break

        else:
            print("Please type add, done, show or back.")


# ---------------------------------------------------------------
# Tool 3: Name Formatter
# Takes a first and last name, tidies the capitalisation and spacing,
# and shows the full name plus initials.
# ---------------------------------------------------------------
def name_formatter():
    print("\n--- Name Formatter ---")
    first = input("First name: ").strip().title()
    last = input("Last name: ").strip().title()

    if first == "" or last == "":
        print("Both a first and last name are needed.")
    else:
        print(f"Formatted name: {first} {last}")
        print(f"Initials: {first[0]}.{last[0]}.")


# ---------------------------------------------------------------
# Main menu loop
# Shows the menu after every tool finishes, until the user quits.
# Any choice that isn't 1-4 gets a polite message instead of a crash.
# ---------------------------------------------------------------
print("Welcome to your Personal Mini-Toolkit!")

while True:
    print("\n=== Personal Mini-Toolkit ===")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Name Formatter")
    print("4. Quit")
    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        guessing_game()
    elif choice == "2":
        todo_list()
    elif choice == "3":
        name_formatter()
    elif choice == "4":
        print("Thanks for using the toolkit. Goodbye!")
        break
    else:
        print(f"Sorry, '{choice}' isn't on the menu. Please choose 1, 2, 3 or 4.")