# coding=utf-8
# author Mher
# importing necessary packages
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    print("Getting the source code...")
    soup = BeautifulSoup(source_code, "html.parser")
    print("Parsing html...")
    # in order to get the proper content, please find a specific pattern
    # that encounters some times, then do as in the following.
    for post_text in soup.findAll('span', {'class': 'grey'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    print("Cleaning up unnecissary characters...")
    for word in word_list:
        symbols ="1234567890`~!@#$%^&*()-_+={}[];\"':<>,"
        for i in range (0, len(symbols)):
            word = word.replace(symbols[i], '')
            if str(len(word)) > 3:
                clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    print("Creating dictionary...")
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)
print ("Completed.")

start("http://spaces.ru/forums/?f=1307&link_id=838708")
