from Crawler import Crawler
import shutil


# centers text in terminal
def center_text(text):
    # number of columns in current terminal window
    col = shutil.get_terminal_size().columns
    return text.center(col)


def execute_terminal_view():
    print(center_text("Welcome to Find Your Beat!"))
    print(center_text("Author: Toby Chow"))
    print("\n\nPlease enter address to crawl (Note: Only default /r/Music Supported at this moment)")
    url_input = input("Enter '1' to select default /r/Music: ").lower()
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
    print(center_text('Congratulations, you have successfully connected to /r/Music'))
    key_words = []
    navigation_menu(url, key_words)


def navigation_menu(url, key_words):
    print(center_text('================'))
    print(center_text('Navigation Menu'))
    print(center_text('================'))
    print(center_text('1 - Search for music'))
    print(center_text('2 - Enter Search Preferences Menu'))
    print(center_text('3 - Enter Taste Breaker Menu'))
    print(center_text('10 - Exit Application'))
    user_input = input().lower()

    accepted = False
    while not accepted:
        if user_input == '1':
            accepted = True
            search_music(url, key_words)
        elif user_input == '2':
            accepted = True
            search_preference_menu(url, key_words)
        elif user_input == '3':
            accepted = True
            taste_breaker_menu(url, key_words)
        elif user_input == '10':
            exit()
        else:
            user_input = input("Please enter a valid input: ").lower()


def search_music(url, key_words):
    print(center_text('==================='))
    print(center_text('Search Music'))
    print(center_text('==================='))
    print(center_text("Enter 's' to search for music!"))
    print(center_text("To quit to The Navigation Menu, enter 'q'"))
    user_input = input().lower()
    accepted = False
    while not accepted:
        if user_input == 's':
            accepted = True
            is_number = False
            pages_input = input("Enter the amount of pages you'd like to search: ").lower()

            # case user wants to exit
            if pages_input is 'q':
                navigation_menu(url, key_words)

            while not is_number:
                if pages_input.isdigit():
                    is_number = True
                else:
                    pages_input = input("Please enter a valid input: ").lower()
            pages = int(pages_input)
            Crawler().item_spider(url, pages, key_words)
            search_music(url, key_words)

        elif user_input == 'q':
            accepted = True
            navigation_menu(url, key_words)
        else:
            user_input = input("Please enter a valid input: ").lower()


# ** add options for default genres
def search_preference_menu(url, key_words):
    print(center_text('========================'))
    print(center_text('Search Preferences Menu'))
    print(center_text('========================'))
    print(center_text("To log a search preference, enter 'e <key word>'. "))
    print(center_text(" * These search preferences will assist in personalizing your searches to fit your taste"))
    print(center_text("To remove an existing entry, enter 'r <key word>. "))
    print(center_text("To quit to The Navigation Menu, enter 'q'"))
    user_input = input().lower()
    accepted = False
    while not accepted:
        if len(user_input) > 2 and user_input[0] is 'e' and user_input[1] is ' ':
            # enter search preference
            key_words.append(user_input[2:])
            print("\nSearch preference '" + user_input[2:] + "' has been added")
            print("Existing Search Preferences: ",)
            print_list(key_words)
            search_preference_menu(url, key_words)
        elif len(user_input) > 2 and user_input[0] is 'r' and user_input[1] is ' ':
            # check if entry in list
            if user_input[2:] not in key_words:
                print("Removal unsuccessful. Keyword is not in list.")
            else:
                # remove existing entry
                key_words.remove(user_input[2:])
                print("\nSearch preference '" + user_input[2:] + "' has been removed")
                print("Existing Search Preferences: ",)
                print_list(key_words)
            search_preference_menu(url, key_words)

        elif user_input == 'q':
            # enter navigation menu
            navigation_menu(url, key_words)
            accepted = True

        else:
            user_input = input("Please enter a valid input: ").lower()


def print_list(key):
    for l in key:
        print(str(l)),


def taste_breaker_menu(url, key_words):
    print(center_text('==================='))
    print(center_text('Taste Breaker Menu'))
    print(center_text('==================='))
    print(center_text("Enter 't' to Break your Taste!"))
    print(center_text("To quit to The Navigation Menu, enter 'q'"))
    user_input = input().lower()
    accepted = False
    while not accepted:
        if user_input == 't':
            # ** add user input proofing
            pages = int(input("Enter the amount of pages you'd like to search: "))
            Crawler().randomizer(url, pages, key_words)
        elif user_input == 'q':
            accepted = True
            navigation_menu(url, key_words)
        else:
            user_input = input("Please enter a valid input: ").lower()
