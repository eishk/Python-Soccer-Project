#!/usr/bin/env python
# coding: utf-8

# In[22]:


import csv
import urllib.request as urllib2
from bs4 import BeautifulSoup
import time


first = ['https://www.transfermarkt.us/fc-chelsea/startseite/verein/631/saison_id/2018', 'https://www.transfermarkt.us/manchester-united/startseite/verein/985/saison_id/2018',
         'https://www.transfermarkt.us/fc-arsenal/startseite/verein/11/saison_id/2018', 'https://www.transfermarkt.us/manchester-city/startseite/verein/281/saison_id/2018']

second = ['https://www.transfermarkt.us/tottenham-hotspur/startseite/verein/148/saison_id/2018', 'https://www.transfermarkt.us/fc-liverpool/startseite/verein/31/saison_id/2018',
         'https://www.transfermarkt.us/fc-everton/startseite/verein/29/saison_id/2018', 'https://www.transfermarkt.us/west-ham-united/startseite/verein/379/saison_id/2018',
         ]

third = ['https://www.transfermarkt.us/leicester-city/startseite/verein/1003/saison_id/2018', 'https://www.transfermarkt.us/fc-southampton/startseite/verein/180/saison_id/2018',
        'https://www.transfermarkt.us/crystal-palace/startseite/verein/873/saison_id/2018', 'https://www.transfermarkt.us/stoke-city/startseite/verein/512/saison_id/2018']

fourth = ['https://www.transfermarkt.us/swansea-city/startseite/verein/2288/saison_id/2018', 'https://www.transfermarkt.us/fc-watford/startseite/verein/1010/saison_id/2018',
         'https://www.transfermarkt.us/newcastle-united/startseite/verein/762/saison_id/2018', 'https://www.transfermarkt.us/west-bromwich-albion/startseite/verein/984/saison_id/2018']

fifth = ['https://www.transfermarkt.us/afc-bournemouth/startseite/verein/989/saison_id/2017', 'https://www.transfermarkt.us/brighton-amp-hove-albion/startseite/verein/1237/saison_id/2017',
        'https://www.transfermarkt.us/fc-burnley/startseite/verein/1132/saison_id/2017', 'https://www.transfermarkt.us/huddersfield-town/startseite/verein/1110/saison_id/2017']

file = open('playersvalue_2018.csv', 'a', encoding='utf8')
writer = csv.writer(file)
writer.writerow(['Name', 'Value', 'Team'])
for url in fifth:
    print(url)
    request = urllib2.Request(url, headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
    page = urllib2.urlopen(request)
    soup = BeautifulSoup(page, 'html.parser')

    team_name = soup.find("h1", itemprop="name").find("span").text

    title_text = soup.find("title").text
    title = title_text.split(' -')[0]

    players = soup.find("table", class_ = "items").find("tbody").find_all("tr", recursive=False)


    for player in players:
        name = player.find("a", class_ = "spielprofil_tooltip").text
        linked = player.find("a", href = True, class_ = "spielprofil_tooltip")
        link = linked['href']
        value = player.find("td", class_ = "rechts hauptlink").text
        value = value[1:].strip()
        if not value:
            value = 0
        elif (value[-1].endswith('m')):
            value = value[:-1]
            value = float(value)
            value = value * 1000000
        else:

            value = value[:-3]
            value = float(value)
            value = value * 1000
        writer.writerow([name, value, team_name])
    time.sleep(5)

file.close()
print("done")


# In[ ]:





# In[ ]:




