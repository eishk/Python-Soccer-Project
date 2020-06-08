#!/usr/bin/env python
# coding: utf-8

# In[31]:


import csv
import urllib.request as urllib2
from bs4 import BeautifulSoup
import time

url = 'https://www.transfermarkt.us/premier-league/transfers/wettbewerb/GB1/plus/?saison_id=2017&s_w=&leihe=0&intern=0&intern=1'
file = open('transfers_2017.csv', 'w', encoding='utf8')
writer = csv.writer(file)
writer.writerow(['Name', 'Position', 'Market Value', 'Actual Fee', 'New Team', 'Old Team'])

request = urllib2.Request(url, headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')


def actual_val(value):
    if (value == "-"):
        return 0
    elif (value == "Free transfer"):
        return 0
    else:
        value = value[1:].strip()
        if not value:
            return 0
        if (value[-1].endswith('m')):
            value = value[:-1]
            value = float(value)
            value = value * 1000000
        else:
            value = value[:-3]
            value = float(value)
            value = value * 1000
    return value

boxes = soup.find("div", class_ = "large-8 columns").find_all("div", class_ = "box", recursive= False)
for box in boxes:
    tables = box.find_all("div", class_ = "responsive-table", recursive= False)
    if (tables):
        team = box.find("h2").find("a").text
        in_play = tables[0]
        in_rows = in_play.find("tbody").find_all("tr")
        for row in in_rows:
            infos = row.find_all("td")
            name = infos[0].find("a", class_ = "spielprofil_tooltip").text
            age = infos[2].text
            position = infos[4].text
            market_value = actual_val(infos[5].text)
            old_team = infos[7].find('a').text
            actual_fee = actual_val(infos[8].find('a').text)
            new_team = team
            writer.writerow([name, position, market_value, actual_fee, new_team, old_team])
        out_play = tables[1]
        out_rows = out_play.find("tbody").find_all("tr")
        for row in out_rows:
            infos = row.find_all("td")
            name = infos[0].find("a", class_ = "spielprofil_tooltip").text
            age = infos[2].text
            position = infos[4].text
            market_value = actual_val(infos[5].text)
            new_team = infos[7].find('a').text
            actual_fee = actual_val(infos[8].find('a').text)
            old_team = team
            writer.writerow([name, position, market_value, actual_fee, new_team, old_team])
file.close()
        
    


# In[ ]:





# In[ ]:




