import requests
from bs4 import BeautifulSoup

#scrap sectors
def scrap_sectors(url):

    # Get Source Code
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    sectors = []

    sectors_section=soup.find(id="tab1")
    sectors_section_table=sectors_section.find("tbody")
    sectors_tr=sectors_section_table.find_all("tr")
    for i in sectors_tr:
        sector_tag=i.find("td").find("a")
        sectors.append("https://www.reuters.com/"+sector_tag.get("href"))
    return sectors

#scrap 1st link here
def scrap_first_link(url):
    # Get Source Code
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    data={}
    header = soup.find(class_="sectionRelatedTopics").find("ul")
    link=header.find("li")
    data[link.find("a").string]="https://www.reuters.com"+link.find("a").get("href")
    return data

#scrap other related industries links
def related_industries(url):

    # Get Source Code
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    related_industries_data = {}

    header=soup.find(class_="sectionRelatedTopics relatedIndustries").find("ul")
    for links in header.find_all("li"):
        related_industries_data[links.string]="https://www.reuters.com"+links.find("a").get("href")

    return related_industries_data

#driver function to gather data, call this function to get links_data dictionary
def get_data():
    # To get all sectors
    sectors_data = scrap_sectors("https://www.reuters.com/sectors/industries/significant?industryCode=4")
    links_data={}

    for sector in sectors_data:
        link=scrap_first_link(sector)
        links_data.update(link)
        print(link)
    print("Completed first link data")

    #updating healthcare reform for url issues for now
    links_data["Healthcare Reform"]="https://www.reuters.com/sectors/industries/overview?industryCode=151"

    related_links_data = {}

    for key, value in links_data.items():
        link = related_industries(value)
        related_links_data.update(link)
        print(link)
    links_data.update(related_links_data)

    print("All links data gathered")
    return links_data