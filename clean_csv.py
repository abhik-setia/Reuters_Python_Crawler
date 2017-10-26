import csv

def get_clean_csv_data():
    industry = []
    perm_id = []
    final_data = []

    with open('data.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)

        for row in csvReader:
            industry.append(row[3])
            perm_id.append(row[4])
        data = list(zip(industry, perm_id))
        for touple in data:
            if touple[0] != '':
                final_data.append(touple)
    dict_data = dict(final_data)

    # with open('clean.csv', 'w',newline="\n",encoding="utf-8") as f:
    #     writer = csv.writer(f)
    #
    #     for key,value in dict_data.items():
    #         writer.writerow([key,value])
    return dict_data

get_clean_csv_data()