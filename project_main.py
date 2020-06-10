'''
Authors: Eish Kapoor, Kunal Bhandarkar
Date: June 1, 2020
Desc: <change this eventually> this file runs basically all the other
files and answers all the questions we wanted to answer
'''

from covid19_total_revenue import get_total_revenue
from covid19_player_value import get_player_value
from qualitative_player_value import get_qualitative_value
from q2_data_analysis import main_analysis


def main():
    get_total_revenue()
    get_qualitative_value()
    main_analysis()

if __name__ == '__main__':
    main()
