'''
Toby Chow
Crawler.py

Class that helps crawl through web pages and take relevant information such as links and images. This information can be then
displayed in an organized manner by the Beautiful Soup package
'''
import urllib3
import certifi
import random
# request info from web page
import requests
# sort through data
from bs4 import BeautifulSoup


class Crawler:
    def item_spider(self, url, pages, key_words):
        counter = 0
        while counter < pages:
            counter = counter+1
            http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data, features="html.parser")

            # gets link to next page
            url = soup.find('span', {'class': 'next-button'}).a['href']

            for link in soup.findAll('a', {'class': 'title may-blank outbound'}):
                title = link.text
                href = link['href']
                title_temp = link.text.lower()
                if len(key_words) is 0:
                    print(title)
                    print(href)
                else:
                    for k in key_words:
                        if title_temp.find(k) is not -1:
                            print(title)
                            print(href)
    '''
    finds a random song that is not part of keywords provided by user. searches through the number of specified pages
    that the user selects. outputs song name and url
    '''

    def randomizer(self, url, max_pages, keywords):
        rand_num = random.randrange(max_pages*25)
        # needs to be odd to have choice be a title
        while rand_num % 2 is not 0:
            rand_num = random.randrange(max_pages * 25)
        music_list = []
        counter = 0
        while counter < max_pages:
            counter = counter + 1
            http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data, features="html.parser")

            url = soup.find('span', {'class': 'next-button'}).a['href']

            for link in soup.findAll('a', {'class':'title may-blank outbound'}):
                # needs to not be contained
                music_list.append(link['href'])
                music_list.append(link.text)
        found = False
        result_title = music_list[rand_num+1]
        result_url = music_list[rand_num]
        while not found:
            if not self.check_keyword(result_title, keywords):
                found = True
                break
            rand_num = random.randrange(max_pages * 25)
            # needs to be odd to have choice be a title
            while rand_num % 2 is not 0:
                rand_num = random.randrange(max_pages * 25)
            result_title = music_list[rand_num+1]
            result_url = music_list[rand_num]

        print(result_title + "\n" + result_url)

    # checks if keyword is in the search result
    # returns true if yes, false if not
    def check_keyword(self, test_string, keywords):
        test_string = test_string.lower()
        for k in keywords:
            # contained
            if test_string.find(k) != -1:
                return True
        return False

    def get_single_item_data(self, item_url):
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
