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


start("http://spaces.ru/forums/?f=1307&link_id=838708")
