'''
Toby Chow
main.py

Main function for Find Your Beat
'''
from Crawler import Crawler

def main():
    url = "https://old.reddit.com/r/Music/"
    key_words = {'rock', 'soul'}
    cr = Crawler().item_spider(url, 5, key_words)
if __name__ == "__main__":
    main()