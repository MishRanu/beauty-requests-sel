from bs4 import BeautifulSoup


def read_file():
    html_file = open("three-sisters.html", 'r')
    read_buffer = html_file.read()
    html_file.close()
    return read_buffer


soup = BeautifulSoup(read_file(), 'lxml')
body = soup.body
# print(body)
print(type(body.contents))
# for element in body.contents:
#     print(element)
print(type(body.children))

# for element in body.children:
#     print(element if element !='\n' else 'NEW_LINE')
#
# p = soup.p
# print(p.next_sibling.next_sibling)

print(len(list(body.descendants)))

# for index, child in enumerate(soup.head.descendants):
#     print(index)
#     print(child if child !='\n' else 'NEW_LINE', end='\n')

p = soup.p
# print(type(p.parent.parent.parent))
print(type(p.parent.parent))

count = 0
print("===========================================")
# for tag in p.parents:
#     # print(tag if tag !='\n' else '', end='\n\n\n')
#     print(type(tag))
#     count+=1
#
# print("number of parents is ", count)

# print(p.next_sibling.next_sibling.next_sibling.next_sibling)
# print(p.previous_sibling.previous_sibling.previous_sibling)

print(type(p.next_siblings))
for element in p.previous_siblings:
    print(element if element!='\n' else 'NEW_LINE')