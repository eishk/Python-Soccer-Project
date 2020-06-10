'''
Authors: Eish Kapoor, Kunal Bhandarkar
Date: June 1, 2020
Desc: executes all files to get information on how the financials of the
Premier League have been affected, how qualitative player descriptions
relate to monetary value, and analysis on player value due to COVID-19
'''

from covid19_total_revenue import get_total_revenue
from qualitative_player_value import get_qualitative_value
from q2_data_analysis import main_analysis


def main():
    '''
    executes all functions imported to answer our three critical questions
    '''
    print('\ntotal revenue info:')
    get_total_revenue()
    print('\ngetting qualitative value numbers:')
    get_qualitative_value()
    print('\nanalysis on player value')
    main_analysis()


if __name__ == '__main__':
    main()
