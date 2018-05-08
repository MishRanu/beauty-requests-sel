from bs4 import BeautifulSoup
import re


def read_file():
    html_file = open("three-sisters.html", 'r')
    read_buffer = html_file.read()
    html_file.close()
    return read_buffer


soup = BeautifulSoup(read_file(), 'lxml')

#signature find_all(name, attrs, recursive, string, limit, **kwargs)

#name parameter
    #regex object - string - True - function

# a_tags = soup.find_all('a')
# for a in a_tags:
#     print(a)

#attrs parameter
attr_1 = {'class': 'sister', 'id':'link1'}
body = soup.body
first_a = body.find_all('a', attrs=attr_1)
print(first_a)

print("===========")

attr = {'class': 'sister'}
asister= soup.find_all('a', attrs=attr)
print(asister)


print("=================")
#limit parameter
a_tags = soup.find_all('a', limit=2)
print(a_tags)

#find_all more parameters

print("================")
#discussing the string parameter
#will accept a regex object that will contain the string in the text

regex_string = re.compile('story')
tag = soup.find_all(string=regex_string)
print(tag)

print("==============")
tag2 = soup.find_all(string='story')
print(tag2)

print("============")
tags_class = soup.find_all(class_='sister')
print(tags_class)
#discussing the recursive parameter

print("==============")
title = soup.find_all('title', recursive=False)
print(title)

print("==============")
title = soup.find_all('title', recursive=True)
print(title)