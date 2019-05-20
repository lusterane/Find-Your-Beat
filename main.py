'''
Toby Chow
main.py

Main function for Find Your Beat
'''

import TerminalView

import CSVHandler
from Crawler import Crawler


def main():
    debug = True

    if debug is True:
        '''
        dict_1 = {'song_title': 'hello', 'link': 'www.hello.com'}
        dict_2 = {'song_title': 'hello1', 'link': 'www.hello1.com'}
        dict_keywords_1 = {'keywords': 'rock'}
        dict_keywords_2 = {'keywords': 'lol'}
        set_1 = []
        set_2 = []
        set_1.append(dict_1)
        set_1.append(dict_2)
        set_2.append(dict_keywords_1)
        set_2.append(dict_keywords_2)
        CSVHandler.write_music_data(set_1)
        CSVHandler.write_key_words(set_2)
        '''

        # initialize music_data.csv
        fieldnames = ['song_title', 'link']
        CSVHandler.initialize_csv('data/music_data.csv', fieldnames)

        Crawler().randomizer()
    else:
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
