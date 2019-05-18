'''
Toby Chow
main.py

Main function for Find Your Beat
'''

import TerminalView


def main():
    valid_input = False

    while not valid_input:
        navigation_input = input("Would you like to navigate using the terminal or GUI? [terminal/gui]")

        if navigation_input.lower() == "terminal":
            # execute terminal
            TerminalView.execute_terminal_view()
            valid_input = True
        elif navigation_input.lower() == "gui":
            # execute gui
            print("gui")
            valid_input = True
        else:
            print("Please enter a valid input")


if __name__ == "__main__":
    main()
