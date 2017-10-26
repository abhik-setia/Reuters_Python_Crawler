import clean_csv
import csv
import related_industries_scraper
import company_scraper
import people_scraper
import os

#this will get us permid and sector name
industry_data=clean_csv.get_clean_csv_data()

#get all links and sectors
sectors_data=related_industries_scraper.get_data()

data=[]

#create a new csv for industries data
for industry_key,industry_value in industry_data.items():
    if industry_key in sectors_data:
        data_tuple=tuple((industry_key, industry_value, sectors_data[industry_key]))
        data.append(data_tuple)
    else:
        data.append(tuple((industry_key, industry_value,"Not Found")))

print("Creating a csv for industries data")

#Storing industry name, permid and url
with open('Industries.csv', 'w',newline="\n",encoding="utf-8") as f:
    writer = csv.writer(f)
    for d in data:
        writer.writerow(d)

print("Industries data csv Saved")

print("Gathering Industries details data")

industry_details_data=[]
industries_links_len=len(data)

for index,d in enumerate(data):
    if d[2] !="Not Found":
        #we need to get industry code
        code=d[2].split("=")[1]
        c_data=company_scraper.scrap_company(industry_code=code)
        for c in c_data:
            single_industry_val=tuple((d[0],d[1],c[0],c[1],c[2],c[3],c[4]))
            industry_details_data.append(single_industry_val)
        os.system('cls')
        print("tickr completed so far : ",str(round(float(index)*100/industries_links_len,2))," %")


print("Industries details data gathered")

print("Creating a csv for Companies ranking data")

# now we will create a csv for industry details
with open('Companies_Data.csv', 'w',newline="\n",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Industry Name","permid","Ticker","Name","Market Capitalisation","TTm Sales","Employees"])
    for d in industry_details_data:
        writer.writerow(d)

print("Companies ranking data saved")

print("Gathering Peoples data")

#now lets gather people's data
people_data=[]
industries_links_len=len(industry_details_data)
for index,data in enumerate(industry_details_data):
    if data[2] is not None:
        p_data=people_scraper.scrape_people(ticker_no=data[2])
        for p in p_data:
            people_data.append(tuple((data[0],data[1],data[2],p[0],p[1],p[2],p[3],p[4])))
        print(p_data)
        #os.system('cls')
        print("People data gathered so far : ",str(round(float(index)*100/industries_links_len,2))," %")

print("People data gathered")

print("Creating a csv for People data")

# now we will create a csv for people details
with open('Poeple_data.csv', 'w',newline="\n",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Industry Name","permid","Ticker","Name","Age","Since","Current Position","Description"])
    for d in people_data:
        writer.writerow(d)

print("People data saved")

print("All Data has been gathered, Thank you for your support")

