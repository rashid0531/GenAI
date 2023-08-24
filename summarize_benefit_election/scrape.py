from bs4 import BeautifulSoup
import requests
import re

def find_nested_paras(beautiful_body_obj):
    nested_paras = beautiful_body_obj.find_all("p")
    if nested_paras:
        for each_para in nested_paras:
            print(each_para.text)


def find_nested_headers(beautiful_body_obj):
    nested_headers = beautiful_body_obj.find("h3", id=re.compile('^a1_9_'))
    if nested_headers:
        print(nested_headers.text)


def find_nested_sections(beautiful_body_obj):
    nested_section = beautiful_body_obj.find_all("section")
    if nested_section:
        for each_nested_section in nested_section:
            nested_paras = find_nested_paras(each_nested_section)
            nested_headers = find_nested_headers(each_nested_section)
        

url_to_scrap = "https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/digest/chapter-1/payment-benefit.html#a1_9_0"
html_text = requests.get(url_to_scrap).text

soup = BeautifulSoup(html_text, 'lxml')

sections = soup.find_all("section")
for each_section in sections:
    each_section_title = each_section.find("h2", id=re.compile('^a1_9_'))
    if each_section_title:
        print(each_section_title.text)
    
    find_nested_sections(each_section)

    

