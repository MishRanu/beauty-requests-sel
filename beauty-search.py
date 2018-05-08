from bs4 import BeautifulSoup
import re

def read_file():
    html_file = open("three-sisters.html", 'r')
    read_buffer = html_file.read()
    html_file.close()
    return read_buffer

soup = BeautifulSoup(read_file(), "lxml")

print(soup.find_all('a'))

regex = re.compile('^b')
for tag in soup.find_all(regex):
    print(tag.name)

regext = re.compile('t')
# print(regext.match("html"))
for tag in soup.find_all(regext):
    print(tag.name)
#
# for tag in soup.find_all(["a", "b"]):
#     print(tag.name)
#
# #the find all function can also accept functions as a parameter
# def has_class(tag):
#     return tag.has_attr('class')
#
# print("============")
# for tag in soup.find_all(has_class):
#     print(tag.name)
#
