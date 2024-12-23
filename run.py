import random
import classes.graphics as graphics

RANDOM_NUMBERS = list(range(10))
CODE_LENGTH = 4
MAX_ATTEMPTS = 11


def main_menu():
    """
    Menu screen with options for player
    """
    graphics.header_image()
    graphics.main_logo()
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
    print("You have a maximum of 12 attempts."
          "Remember a number can appear more than once.\n")
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

    attempt_number = 0
    original_answer = generate_code()

    while attempt_number <= MAX_ATTEMPTS:
        user_guess = user_guess_input(attempt_number)
        modified_answer = list(original_answer)

        print(f"{display_user_guess(user_guess)}\n")

        position, number = check_result(user_guess, modified_answer)
        if position == CODE_LENGTH:
            graphics.you_win()
            print("You guessed the code correctly!")
            print(f"The secret code is: "
                  f"{display_user_guess(original_answer)}\n")
            print(f"You cracked the code in {attempt_number} attempts.\n")
            print("Would you like to play again? (Y/N)")
            play_again()
            break

        elif attempt_number == MAX_ATTEMPTS and position != CODE_LENGTH:
            graphics.game_over()
            print(f"The secret code was: "
                  f"{display_user_guess(original_answer)}\n")
            print("You were unable to guess the code. Try again? (Y/N)")
            play_again()
            break

        else:
            attempt_number += 1
            print(f"Correct number and position: {position}")
            print(f"Correct number, but incorrect position: {number}")
            print(f"You have {MAX_ATTEMPTS - attempt_number + 1}"
                  f" attempts remaining.\n")


def user_guess_input(attempt):
    """
    Asks the user to enter their guess and validates it.
    Outputs ValueError if the input is invalid.
    """
    while True:
        try:
            guess = input(f"Attempt {attempt + 1}: "
                          f"Enter your 4-digit guess: ").strip()

            if len(guess) != CODE_LENGTH or not guess.isdigit():
                raise ValueError(f"Invalid - please enter exactly"
                                 f"{CODE_LENGTH} digits.\n")

            guess_list = [int(digit) for digit in guess]
            return guess_list

        except ValueError as e:
            print(e)


def display_user_guess(guess):
    """
    Displays the user's guess.
    """
    return ''.join(str(digit) for digit in guess)


def check_result(user_guess, original_answer):
    """
    Checks the user's guess against the original answer.
    Returns the number of digits that are correct and in the correct position
    and the number of correct digits that are in the wrong position.
    """
    position = 0
    number = 0

    modified_answer = original_answer.copy()

    for i in range(CODE_LENGTH):
        if user_guess[i] == modified_answer[i]:
            position += 1
            modified_answer[i] = None
            user_guess[i] = -1

    for digit in user_guess:
        if digit in modified_answer:
            number += 1
            modified_answer[modified_answer.index(digit)] = None

    return position, number

main_menu()