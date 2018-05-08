from bs4 import BeautifulSoup
import requests
import os


class CodingBatScraper(object):

    @staticmethod
    def read_file(file_name):
        file = open(file_name, 'r')
        data = file.read()
        file.close()
        return data

    @staticmethod
    def write_file(file_name, data):
        file = open(file_name, 'w')
        file.write(data)
        file.close()

    def __init__(self, base_url):
        self.base_url = base_url
        os.mkdir("sections")
        self.scrape_website(self.base_url + "/java")

    def scrape_question(self, section_name, question_name, question_url):
        # print("scraping question from section: {}, question_name: {}, question_url: {}".format(section_name, question_name, question_url))
        question_request = requests.get(question_url)
        question_file_name = "sections/" + section_name + "/" + question_name + ".html"
        CodingBatScraper.write_file(question_file_name, question_request.text)
        question_soup = BeautifulSoup(CodingBatScraper.read_file(question_file_name), 'lxml')
        question_div = question_soup.find('div', class_="minh")
        question = question_div.p.string
        output= ""
        for element in question_div.next_siblings:
            if element.name == "br":
                output += element.next_sibling
                output += "\n"
        output = output.strip()
        print("The question is: \n", question)
        print("The outputs are: \n", output)

    def scrape_section(self, section_name, url):
        print(section_name, url)
        os.mkdir("sections/" + section_name)
        questions_request = requests.get(url)
        section_file_name = "sections/" + section_name + "/" + section_name + ".html"
        CodingBatScraper.write_file(section_file_name, questions_request.text)
        section_soup = BeautifulSoup(CodingBatScraper.read_file(section_file_name), 'lxml')
        attr = {
            'src':'/c1.jpg'
        }
        questions_divs = section_soup.find_all('img', attrs=attr)
        for question_div in questions_divs:
            self.scrape_question(section_name, question_div.next_sibling.string, self.base_url + question_div.next_sibling['href'])

    def scrape_website(self, base_url):
        print("inside scrape website")
        website_request = requests.get(base_url)
        CodingBatScraper.write_file("website_page.html", website_request.text)

        website_soup = BeautifulSoup(CodingBatScraper.read_file("website_page.html"), 'lxml')
        section_divs = website_soup.find_all('div', class_="summ")

        for section_div in section_divs:
            self.scrape_section(section_div.a.span.text, self.base_url + section_div.a["href"])

        # os.rmdir("./sections")


CodingBatScraper("http://codingbat.com")
