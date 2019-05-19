import csv

'''
writes a set of dictionaries into csv file stored in /data directory
stores music results from searches
'''
def write_music_data(m_set):
    with open('data/music_data.txt', mode='w', newline='') as music_file:
        fieldnames = ['song', 'link']
        music_writer = csv.DictWriter(music_file, fieldnames=fieldnames)

        music_writer.writeheader()
        for m_dict in m_set:
            music_writer.writerow(m_dict)


'''
writes a set of dictionaries into csv file stored in /data directory
stores keywords for search preferences
'''
def write_key_words(k_set):
    with open('data/key_words.txt', mode='w', newline='') as key_file:
        fieldnames = ['keywords']
        key_writer = csv.DictWriter(key_file, fieldnames=fieldnames)

        key_writer.writeheader()
        for key in k_set:
            key_writer.writerow(key)

