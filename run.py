#menu screen
def main_menu():
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


main_menu()