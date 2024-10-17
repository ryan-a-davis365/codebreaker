import random

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
                run_game()
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
    
main_menu()