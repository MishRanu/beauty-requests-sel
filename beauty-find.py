from bs4 import BeautifulSoup
import re

#find() function is the same as find_all() just that the limit is set to 1
#so if there are five search results, it will return the first tag

def read_file():
    html_file = open("three-sisters.html", 'r')
    read_buffer = html_file.read()
    html_file.close()
    return read_buffer

soup = BeautifulSoup(read_file(), 'lxml')
tag = soup.find('a')
print(tag)
