'''
Toby Chow
Web Crawler Application

Crawls through web pages and takes relevant information such as links and images. This information is then
displayed in an organized manner by the Beautiful Soup package
'''

# request info from web page
import requests
# sort through data
from bs4 import BeautifulSoup

'''crawls a search in Walmart's database for "billiards". Each search result gives information of its link
and title to be printed. This can be done for however many pages of search results the user desires.
'''


def item_spider(max_pages):
    page = 1
    while page < max_pages+1:
        url = 'https://www.walmart.com/search/?page=' + str(page) + '&query=billiards#searchProductResult'
        page += 1
        # all of inspect element information
        source_code = requests.get(url)
        # takes only the "text" ie. links, images
        plain_text = source_code.text

        # to organize into beautiful soup
        soup = BeautifulSoup(plain_text, features="html.parser")
        for link in soup.findAll('a', {'class': 'product-title-link line-clamp line-clamp-2'}):
            # gets the link of each title
            href = 'https://www.walmart.com'+link.get('href')
            # the text of the link, aka name
            title = link.get('aria-label')
            # print(href)
            print(title)
            get_single_item_data(href)

'''
finds all the links of a given url and prints them
'''


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    # prints the company for each item
    '''
    for item_name in soup.findAll('span', {'itemprop': 'brand'}):
        print(item_name.string)
    '''
    # prints ALL the links of a page
    for link in soup.findAll('a'):
        current = str(link.get('href'))
        # in case href attribute is not found under 'a' tag
        if current != 'None':
            # in case link does not provide home address
            if current.startswith('https://'):
                print(current)
            else:
                print('https://www.walmart.com'+current)


item_spider(1)
