from bs4 import BeautifulSoup


def read_file():
    file = open("tags.html", 'r')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')
body = soup.body
print(body['class'])
p = soup.p
body['style'] = "Some inner html"
print(body.get('style'))
print(p)
print("printing", p.string.replace_with('Changed in the first div'))
p.string.replace_with('Changed in the first div')
print(p['style'])
print(body.string)

# print(soup.prettify())