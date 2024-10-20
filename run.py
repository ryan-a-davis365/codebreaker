#import
import random

#constants
RANDOM_NUMBERS = list(range(10))
CODE_LENGTH = 4
MAX_ATTEMPTS = 8

#menu screen
def main_menu():
    """
    Menu screen with options for player
    """
    print("Press 1 to play. Press 2 for instructions. Press 3 to exit.")

    while True:
        try:
            menu_select = int(input("Press key: \n"))
            if menu_select == 1:
                start_game()
                break
            elif menu_select == 2:
                instructions()
                break
            elif menu_select == 3:
                print("""
                   Exiting game...

                   ...Game closed.
                """)
                break
            else:
                raise ValueError

        except ValueError:
            print("""
            Invalid key pressed. Please choose one of the following:\n
            Press 1 to play. Press 2 for instructions. Press 3 to exit.
            """)


def instructions():
    """
    Instructions for the user about how to play
    """

    print("A secret code of 4 numbers will be randomly generated.\n")
    print("Your challenge is to find what numbers the code consists off.\n")
    print("You have a maximum of 6 attempts. Remember a number can appear more than once.\n")
    print("Only guess a 4 number code with no commas or spaces.\n")
    print("Are you ready? (Y to play, N to return to the menu)")

    play_again()


def play_again():
    """
    Checks if the player entered Y or N correctly,
    and directs them to the game or menu.
    """
    while True:
        try:
            play_again_choice = (input("Enter choice: \n")).upper().strip()
            if play_again_choice == "Y":
                start_game()
                break
            elif play_again_choice == "N":
                main_menu()
                break
            else:
                raise ValueError

        except ValueError:
            print("""
            Invalid key pressed.
            Press Y to play the game, or N to return to the main menu.
            """)


def generate_code():
    """
    Generates a 4-number code. Duplicates are enabled
    """
    number_code = []
    while len(number_code) < CODE_LENGTH:
        random_number = random.choice(RANDOM_NUMBERS)
        number_code.append(random_number)
    return number_code


def start_game():
    """
    Starts the main game functions
    """
    print("Guess the 4 digit number:")

    original_answer = generate_code()
    attempt_number = 0

    while attempt_number <= MAX_ATTEMPTS:
        user_guess = user_guess_input(attempt_number)
        modified_answer = list(original_answer)

        print(f"{display_user_guess(user_guess)}\n")

        position, number = check_result(user_guess, modified_answer)
        if position == CODE_LENGTH:
            print("You guess the code correctly!")
            print(f"The secret code is: {display_user_guess(original_answer)}\n")
            print(f"You cracked the code in {attempt_number} attempts.\n")
            print("Would you like to play again? (Y/N)")
            play_again()
            break
        
        elif attempt_number == MAX_ATTEMPTS and position != CODE_LENGTH:
            print(f"The secret code was: {display_user_guess(original_answer)}\n")
            print("You were unable to guess the code. Try again? (Y/N)")
            play_again()
            break
        
        else:
            attempt_number += 1
            print(f"Correct number and position: {position}")
            print(f"Correct number, but incorrect position: {number}")
            print(f"You have {MAX_ATTEMPTS - attempt_number + 1} attempts remaining.\n")


def user_guess_input(attempt):
    """
    Asks the user to enter their guess and validates it.
    Outputs ValueError if the input is invalid.
    """
    while True:
        try:
            

main_menu()
start_game()