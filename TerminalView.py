from TerminalFormatter import TermForm
from Crawler import Crawler


global_form_col = -1


def set_global():
    global global_form_col
    global_form_col = TermForm().columns


def execute_terminal_view():
    print("Welcome to Find Your Beat!".center(global_form_col))
    print("Author: Toby Chow".center(global_form_col))
    print("\n\nPlease enter address to crawl (Note: Only default /r/Music Supported at this moment)")
    url_input = input("Enter '1' to select default /r/Music: ")
    url = ''
    if url_input == '1' or url_input.find('reddit.com/r/Music/') is not -1:
        url = "https://old.reddit.com/r/Music/"
    else:
        accepted = False
        while not accepted:
            url_input = input("Please enter a valid input: ")
            if url_input == '1' or url_input.find('reddit.com/r/Music/') is not -1:
                url = "https://old.reddit.com/r/Music/"
                accepted = True
    print('Congragulations, you have successfully connected to /r/Music'.center(global_form_col))
    key_words = []
    navigation_menu(url, key_words)


def navigation_menu(url, key_words):
    accepted = False
    while not accepted:
        print('================'.center(global_form_col))
        print('Navigation Menu'.center(global_form_col))
        print('================'.center(global_form_col))
        print('1 - Search for music'.center(global_form_col))
        print('2 - Enter Search Preferences Menu'.center(global_form_col))
        print('3 - Enter Taste Breaker Menu'.center(global_form_col))
        print('10 - Exit Application'.center(global_form_col))
        user_input = input()

        if user_input == '1':
            search_music(url, key_words)
        elif user_input == '2':
            search_preference_menu(url, key_words)
        elif user_input == '2':
            taste_breaker_menu(url, key_words)
        elif user_input == '10':
            exit()
        else:
            print('Please enter a valid input')


def search_music(url, key_words):
    accepted = False
    while not accepted:
        print('==================='.center(global_form_col))
        print('Search Music'.center(global_form_col))
        print('==================='.center(global_form_col))
        print("Enter 's' to search for music!".center(global_form_col))
        print("To quit to The Navigation Menu, enter 'q'".center(global_form_col))
        user_input = input()

        if user_input == 's':
            # ** add user input proofing
            pages = int(input("Enter the amount of pages you'd like to search: "))
            Crawler().item_spider(url, pages, key_words)

        elif user_input == 'q':
            accepted = True
            navigation_menu(url, key_words)
        else:
            print('Please enter a valid input')


# ** add options for default genres
def search_preference_menu(url, key_words):
    accepted = False
    while not accepted:
        print('========================'.center(global_form_col) +
              '\nSearch Preferences Menu\n'.center(global_form_col) +
              '========================'.center(global_form_col))
        print("To log a search preference, enter 'e <key word>'. ".center(global_form_col))
        print(" * These search preferences will assist in personalizing your searches to fit your taste".center(global_form_col))
        print("To remove an existing entry, enter 'r <key word>. ".center(global_form_col))
        print("To quit to The Navigation Menu, enter 'q'".center(global_form_col))
        user_input = input()
        if user_input[0] == 'e':
            # enter search preference
            key_words.append(user_input[2:].lower())
            print("\nSearch preference '" + user_input[2:] + "' has been added")
            print("Existing Search Preferences: ",)
            print_list(key_words)
        elif user_input[0] == 'r':
            # remove existing entry
            key_words.remove(user_input[2:].lower())
            print("\nSearch preference '" + user_input[2:] + "' has been removed")
            print("Existing Search Preferences: ",)
            print_list(key_words)

        elif user_input == 'q':
            # enter navigation menu
            navigation_menu(url, key_words)
            accepted = True

        else:
            print("Please enter a valid input")


def print_list(key):
    for l in key:
        print(str(l)),


def taste_breaker_menu(url, key_words):
    accepted = False
    while not accepted:
        print('==================='.center(global_form_col) +
              '\nTaste Breaker Menu\n'.center(global_form_col) +
              '==================='.center(global_form_col))
        print("\nEnter 't' to Break your Taste!".center(global_form_col))
        print("To quit to The Navigation Menu, enter 'q'".center(global_form_col))
        user_input = input()
        if user_input == 't':
            # ** add user input proofing
            pages = int(input("Enter the amount of pages you'd like to search: "))
            Crawler().randomizer(url, pages, key_words)
        elif user_input == 'q':
            accepted = True
            navigation_menu(url, key_words)
        else:
            print('Please enter a valid input')
