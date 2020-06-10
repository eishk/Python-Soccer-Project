"""
Eish Kapoor & Kunal Bhandarkar
CSE 163 AD
Final Project

This file contains the code that uses the BeautifulSoup library
to scrape the TransferMarkt database for the transfers that occurred
in the British Premier League. Includes transfers in and out, and scrapes
the player's name, position, market value, actual fee paid, new team, and
old team.
"""

import csv
import urllib.request as urllib2
from bs4 import BeautifulSoup


def scrape_transfer_data():
    """
    Method that preprocesses the years and feeds the correct url and
    file name to the function necessary for creating the csv of
    soccer transfers for listed years.
    """
    year = ['2017', '2018', '2020']
    url = 'https://www.transfermarkt.us/premier-league/transfers/wettbewerb/'
    'GB1/plus/?saison_id=2017&s_w=&leihe=0&intern=0&intern=1'
    url_begin = 'https://www.transfermarkt.us/premier-league/transfers'
    '/wettbewerb/GB1/plus/?saison_id='
    url_end = '&s_w=&leihe=0&intern=0&intern=1'
    for y in year:
        url = url_begin + y + url_end
        file_path = 'transfers_' + y + '.csv'
        write_transfer_file(url, file_path)


def write_transfer_file(url, file_path):
    """
    Takes given website url and given file_path, and appends to the file
    specified by the file_path rows containing the transfer information for
    every player transferred in and out of the British Premier League in the
    season specified by the TransferMarkt url. Writes row for each player in
    the form of ['Name', 'Position', 'Market Value', 'Actual Fee', 'New Team',
    'Old Team'].
    """
    file = open(file_path, 'w', encoding='utf8')
    writer = csv.writer(file)
    writer.writerow(['Name', 'Position', 'Market Value', 'Actual Fee',
                    'New Team', 'Old Team'])
    request = urllib2.Request(url,
                              headers={'user-agent': 'Mozilla/5.0 '
                                       '(Macintosh; Intel Mac OS'
                                       ' X 10_14_6)'
                                       ' AppleWebKit/537.36 (KHTML,'
                                       ' like Gecko) Chrome/81.0.'
                                       '4044.138'
                                       'Safari/537.36'})
    page = urllib2.urlopen(request)
    soup = BeautifulSoup(page, 'html.parser')
    b = soup.find("div", class_="large-8 columns")
    boxes = b.find_all("div", class_="box", recursive=False)
    for box in boxes:
        tables = box.find_all("div", class_="responsive-table",
                              recursive=False)
        if (tables):
            team = box.find("h2").find("a").text
            in_play = tables[0]
            in_rows = in_play.find("tbody").find_all("tr")
            for row in in_rows:
                infos = row.find_all("td")
                name = infos[0].find("a", class_="spielprofil_tooltip").text
                position = infos[4].text
                market_value = actual_val(infos[5].text)
                old_team = infos[7].find('a').text
                actual_fee = actual_val(infos[8].find('a').text)
                new_team = team
                writer.writerow([name, position, market_value, actual_fee,
                                new_team, old_team])
            out_play = tables[1]
            out_rows = out_play.find("tbody").find_all("tr")
            for row in out_rows:
                infos = row.find_all("td")
                name = infos[0].find("a", class_="spielprofil_tooltip").text
                position = infos[4].text
                market_value = actual_val(infos[5].text)
                new_team = infos[7].find('a').text
                actual_fee = actual_val(infos[8].find('a').text)
                old_team = team
                writer.writerow([name, position, market_value,
                                actual_fee, new_team, old_team])
    file.close()


def actual_val(value):
    """
    Helper function for taking the given value and converting
    it into a format that can be used for further processing of
    data for the tasks. Turns all the unknown data into zero, free
    transfers into zero, and turns given fees into their numerical
    values without the dollar sign.
    """
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
