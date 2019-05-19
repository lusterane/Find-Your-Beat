'''
Toby Chow
main.py

Main function for Find Your Beat
'''

import TerminalView
import CSVHandler


def main():
    dict_1 = {'song': 'hello', 'link': 'www.hello.com'}
    dict_2 = {'song': 'hello1', 'link': 'www.hello1.com'}
    dict_keywords = {'keywords': 'rock'}
    set_1 = []
    set_2 = []
    set_1.append(dict_1)
    set_1.append(dict_2)
    set_2.append(dict_keywords)
    CSVHandler.write_music_data(set_1)
    CSVHandler.write_key_words(set_2)
    valid_input = False
    while not valid_input:
        navigation_input = input("Would you like to navigate using the terminal or GUI? [terminal/gui]: ")

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
