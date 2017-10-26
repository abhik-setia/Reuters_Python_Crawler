import requests
from bs4 import BeautifulSoup
import exception_handling

@exception_handling.retry()
def scrap_company(url="https://www.reuters.com/sectors/industries/rankings?industryCode",industry_code="179"):

    r = requests.get(url+"="+industry_code+"&page=-1")
    soup = BeautifulSoup(r.content, 'html5lib')

    company_section_full = soup.find(class_="column1 gridPanel grid8")
    company_section = company_section_full.find(class_="dataSmall")

    # define variables
    tickers = []
    names = []
    market_captialization = []
    ttm = []
    employee = []

    for company in company_section.find_all("tr"):
        company_td_all = company.find_all("td")
        for index, company_td in enumerate(company_td_all):
            if index == 0:
                a_tag = company_td.find("a")
                if a_tag is not None:
                    tickers.append(a_tag.string)
            elif index == 1:
                a_tag = company_td.find("a")
                if a_tag is not None:
                    names.append(a_tag.string)
            elif index == 2:
                market_captialization.append(company_td.string)
            elif index == 3:
                ttm.append(company_td.string)
            else:
                employee.append(company_td.string)

    data=list(zip(tickers,names,market_captialization,ttm,employee))
    return data

#example
#company_data=scrap_company(industry_code="4")
#print("Company Data Gathered")
#print(company_data)
