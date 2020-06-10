'''
Authors: Eish Kapoor, Kunal Bhandarkar
Date: June 1, 2020
Desc: <change this eventually> this file runs basically all the other
files and answers all the questions we wanted to answer
'''

from covid19_total_revenue import get_total_revenue
from covid19_player_value import get_player_value
from qualitative_player_value import get_qualitative_value
from transfers_scrape import scrape_transfer_data
from market_values_scrape import scrape_values_data
from q2_data_analysis import main_analysis


def main():
    get_total_revenue(11.53)
    get_player_value(10.00)
    get_qualitative_value('basketball > soccer')
    scrape_transfer_data()
    scrape_values_data()
    main_analysis()

if __name__ == '__main__':
    main()
