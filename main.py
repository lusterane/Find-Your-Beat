'''
Toby Chow
main.py

Main function for Find Your Beat
'''
from Crawler import Crawler

def main():

    url = "https://old.reddit.com/r/Music/"
    key_words = {'rock', 'soul'}
    Crawler().randomizer(url, 2, key_words)

if __name__ == "__main__":
    main()