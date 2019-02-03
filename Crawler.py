'''
Toby Chow
Crawler.py

Class that helps crawl through web pages and take relevant information such as links and images. This information can be then
displayed in an organized manner by the Beautiful Soup package
'''
import urllib3
import certifi
# request info from web page
import requests
# sort through data
from bs4 import BeautifulSoup


class Crawler:
    def item_spider(self, url, pages, key_words):
        counter = 0
        while(counter < pages):
            counter = counter+1
            http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data,features="html.parser")

            # gets link to next page
            url = soup.find('span', {'class':'next-button'}).a['href']
            for link in soup.findAll('a', {'class':'title may-blank outbound'}):
                title = link.text.lower()
                for k in key_words:
                    if title.find(k) is not -1:
                        print(title)


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
                    print('https://www.walmart.com' + current)