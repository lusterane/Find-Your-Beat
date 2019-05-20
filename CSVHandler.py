import csv
import pandas

'''
appends a set of dictionaries into csv file stored in /data directory
d_set - the set of dictionaries to input into csv
file_dir - path to file to write/append to
mode - mode to write or append for csv
fieldnames - header names of csv
'''
def write_data(d_set, file_dir,  fieldnames):
    # encoding in utf-8 fixes UnicodeEncodingError
    with open(file_dir, mode='a', newline='', encoding="utf-8") as music_file:
        music_writer = csv.DictWriter(music_file, fieldnames=fieldnames)

        for d_dict in d_set:
            music_writer.writerow(d_dict)

'''
initializes csv file by overwriting previous data and creating a header
'''
def initialize_csv(file_dir, fieldnames):
    with open(file_dir, mode='w', newline='') as new_csv:
        new_writer = csv.DictWriter(new_csv, fieldnames=fieldnames)
        new_writer.writeheader()
'''
reads csv file with pandas
'''
def read_csv_file(csv_name):
    rd = pandas.read_csv(csv_name)
    return rd