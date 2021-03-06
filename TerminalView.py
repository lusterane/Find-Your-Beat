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
    key_words = []
    search_preference_menu(url, key_words)


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
    print(center_text("Enter 's' to start searching for music!"))
    print(center_text("To quit to The Navigation Menu, enter 'q'"))
    user_input = input().lower()
    accepted = False
    while not accepted:
        if user_input == 's':
            accepted = True

            stop_searching = False
            while not stop_searching:
                # start searching 5 pages
                Crawler().item_spider(url, 5, key_words)

                # read the items in music_data


                search_more_input = input("Not enough options? Enter 'y' to search for more! Other wise, enter 'q' to return to navigation\n\n")

                valid_input = False
                while not valid_input:
                    # if user wants to exit
                    if search_more_input is 'q':
                        valid_input = True
                        stop_searching = True
                        navigation_menu(url, key_words)
                    # else if user wants to search for more
                    elif search_more_input is 'y':
                        valid_input = True
                    else:
                        search_more_input = input("Please enter a valid input: ")


# ** add options for default genres
def search_preference_menu(url, key_words):
    print(center_text('========================'))
    print(center_text('Search Preferences Menu'))
    print(center_text('========================'))
    print(center_text("What type of music do you like? (ex. rock, hip-hop, country, etc.)"))
    print(center_text("Made a mistake? Remove with 'r <music preference>'. (ex. r rock)"))
    print(center_text("Don't have any more preferences? Enter 'q' to go to the Navigation Menu"))
    user_input = input().lower()
    accepted = False
    while not accepted:
        if len(user_input) > 2 and user_input[0] is 'r' and user_input[1] is ' ':
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
            # break out of loop
            accepted = True

            # enter navigation menu
            navigation_menu(url, key_words)
        else:
            # enter search preference
            accepted = True
            key_words.append(user_input)
            print("\nSearch preference '" + user_input + "' has been added")
            print("Existing Search Preferences: ", end="")
            print_list(key_words)
            search_preference_menu(url, key_words)


def print_list(key):
    for l in key:
        print(str(l) + ",", end=" ")

    print()


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
            accepted = True
            pages = input("Enter the amount of pages you'd like to search: ")
            # if user wants to exit
            if pages is 'q':
                taste_breaker_menu(url, key_words)
            # error handling
            digit = False
            while not digit:
                if not pages.isdigit():
                    pages = input("Please enter a valid input: ").lower()
                else:
                    digit = True
            Crawler().randomizer(url, int(pages), key_words)
        elif user_input == 'q':
            accepted = True
            navigation_menu(url, key_words)
        else:
            user_input = input("Please enter a valid input: ").lower()
