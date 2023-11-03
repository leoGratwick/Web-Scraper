import pandas as pd
import requests
from bs4 import BeautifulSoup
import responses



def scrapeCompanies():
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.table.tbody
    rows = table.find_all("tr")

    data = []
    for row in rows:

        #print(row)
        sections = row.find_all("td")
        #print(sections)
        dictionary = {}
        if len(sections) > 6:

            dictionary["Name"] = sections[0].text.strip()
            dictionary["Type"] = sections[1].text.strip()
            dictionary["Revenue"] = sections[2].text.strip()
            dictionary["Profit"] = sections[3].text.strip()
            dictionary["Employees"] = sections[4].text.strip()
            dictionary["Country"] = sections[5].text.strip()

            data.append(dictionary)


    #print(data)

    df = pd.DataFrame(data)
    df.index += 1
    df.to_csv("topCompanies.csv")






if __name__ == '__main__':
    scrapeCompanies()

