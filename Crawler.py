'''
Toby Chow
Crawler.py

Class that helps crawl through web pages and take relevant information such as links and images. This information can be then
displayed in an organized manner by the Beautiful Soup package
'''
import urllib3
import certifi
import random
import CSVHandler
import configparser

# request info from web page
import requests

# sort through data
from bs4 import BeautifulSoup


class Crawler:
    '''
    finds relevant music according to list of keywords
    '''
    def item_spider(self):
        # get configuration information (default is https://old.reddit.com/r/Music/ for url and 3 for pages)
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        url = parser['USER']['url']
        pages = int(parser['USER']['pages'])

        counter = 0
        while counter < pages:
            counter = counter+1
            http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data, features="html.parser")

            # gets link to next page (reuses old url variable)
            url = soup.find('span', {'class': 'next-button'}).a['href']

            # gets information from key_words.csv and places into a list
            key_words = CSVHandler.read_csv_file('data/key_words.csv').values.tolist()

            # list of dictionaries to place into csv
            dict_ls = []

            for link in soup.findAll('a', {'class': 'title may-blank outbound'}):
                title = link.text
                href = link['href']
                title_temp = link.text.lower()
                if len(key_words[0]) is 0:
                    # set title and link in dictionary format for pandas
                    temp_dict = {'song_title': title, 'link': href}
                    dict_ls.append(temp_dict)
                else:
                    for k in key_words:
                        if title_temp.find(k[0]) is not -1:
                            temp_dict = {'song_title': title, 'link': href}
                            dict_ls.append(temp_dict)
            # place into csv file
            fieldnames = ['song_title', 'link']
            file_dir = 'data/music_data.csv'
            CSVHandler.write_data(dict_ls, file_dir, fieldnames)
    '''
    finds 3 random songs that is not part of keywords provided by user. 
    '''
    def randomizer(self):
        # get configuration information (default is https://old.reddit.com/r/Music/ for url and 3 for pages)
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        url = parser['USER']['url']
        pages = int(parser['USER']['pages'])

        # read keyword information
        keywords = CSVHandler.read_csv_file('data/key_words.csv').values.tolist()

        rand_num = random.randrange(pages*25)
        # needs to be odd to have choice be a title
        while rand_num % 2 is not 0:
            rand_num = random.randrange(pages * 25)
        music_list = []
        counter = 0
        while counter < pages:
            counter = counter + 1
            http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
            response = http.request('GET', url)
            soup = BeautifulSoup(response.data, features="html.parser")

            url = soup.find('span', {'class': 'next-button'}).a['href']

            for link in soup.findAll('a', {'class': 'title may-blank outbound'}):
                # needs to not be contained
                music_list.append(link['href'])
                music_list.append(link.text)
        result_title = music_list[rand_num+1]
        result_url = music_list[rand_num]

        # list to hold dictionaries of music
        d_list = []

        # counter to count number of songs found
        song_counter = 0
        found = False
        while not found:
            # break out once done
            if song_counter == 3:
                found = True
                break
            rand_num = random.randrange(pages * 25)
            # needs to be odd to have choice be a title
            while rand_num % 2 is not 0:
                rand_num = random.randrange(pages * 25)
            result_title = music_list[rand_num+1]
            result_url = music_list[rand_num]
            if self.check_duplicate(d_list) and self.check_keyword(result_title, keywords):
                d_list.append({'song_title': result_title, 'link': result_url})
                song_counter += 1
            print(song_counter)

        # place results into music_data.csv
        fieldnames = ['song_title', 'link']
        file_dir = 'data/music_data.csv'
        CSVHandler.write_data(d_list, file_dir, fieldnames)

    # checks if keyword is in the search result
    # returns true if not in search result, otherwise returns false
    def check_keyword(self, test_string, keywords):
        test_string = test_string.lower()
        for k in keywords:
            # contained
            if test_string.find(k[0]) != -1:
                return False
        return True

    # checks duplicates in list
    # returns true if no duplicates otherwise returns false
    def check_duplicate(self, d_list):
        return True

    # check valid song
    # some results are articles/ads
    # songs will have [ ] with genre in-between. More often than not, articles and ads will not
    # will return the Genre inbetween [ ]. If none, will return None (null)
    def check_valid_song(self, song_name):
        return None
