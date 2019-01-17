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


def item_spider(max_pages):
    page = 1
    while page < max_pages:
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
            print(href)
            print(title)


item_spider(2)

