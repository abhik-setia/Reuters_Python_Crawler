import requests
from bs4 import BeautifulSoup
import exception_handling

@exception_handling.retry()
def scrape_people(url="https://www.reuters.com/finance/stocks/company-officers/",ticker_no="1234"):

        #Get Source Code
        source_code=requests.get(url+ticker_no)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,'html.parser')

        people_section_full=soup.find(class_="column1 gridPanel grid8")

        #If people section not present

        people_section=people_section_full.find(class_="dataSmall")

        if people_section is None:
            return []

        #define variables
        names=[]
        age=[]
        since=[]
        current_position=[]
        descriptions=[]

        #To fetch Name,age,since,current_position
        for people in people_section.find_all("tr"):
            people_td_all=people.find_all("td")
            for index,people_td in enumerate(people_td_all):
                name=people_td.find("a",class_="link")
                if name is not None:
                    clean_name=name.string.strip()
                    clean_names=' '.join(clean_name.split("\xa0"))
                    names.append(clean_names)
                if index==1:
                    age.append(people_td.string)
                elif index==2:
                    since.append(people_td.string)
                else:
                    if people_td.string is not None:
                        current_position.append(people_td.string.strip())

        description_section=people_section_full.find_all(class_="dataSmall")[1]

        #To fetch Description
        for bio_section in description_section.find_all("tr"):
            bio_section_td=bio_section.find_all("td")
            for index,bio in enumerate(bio_section_td):
                if index==1:
                    descriptions.append(bio.string.strip())

        data=list(zip(names,age,since,current_position,descriptions))
        return data
#example
#d=scrape_people(ticker_no="ADTR.PK")
#print(d)
