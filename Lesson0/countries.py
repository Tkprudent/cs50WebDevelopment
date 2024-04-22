import csv

def countryList():
    countryLst = []
    with open("countrylist.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            countryLst.append(row['\ufeffcountry'])
    return countryLst

countryList()