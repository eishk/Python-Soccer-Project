'''
Authors: Eish Kapoor, Kunal Bhandarkar
Date: June 1, 2020
Desc: this file answers the question:
What will the effect of COVID-19 be on the total revenue of the Premier League?
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def test_dfs():
    '''
    test_dfs runs functions and makes sure that they return correct values
    throws exception if function performs incorrectly
    '''
    # test extrapolate_2020_data with input test_17 and test_18
    test_17 = pd.DataFrame({
        'Club': ['Club one', 'Turnover', 'Wages', 'Club four'],
        'Test Column': [1]*4,
        'Extra Test': [0]*4
    })
    test_18 = pd.DataFrame({
        'Club': ['Club 1', 'Turnover', 'Wages', 'Club Four'],
        'Test Column': [2]*4,
        'Extra Test': [0]*4
    })

    expected = pd.DataFrame({
        'Club': ['Turnover', 'Wages'],
        'Test Column': [(2-1)*2 + 2]*2,     # 2*(v18 - v17) + v18
        'Extra Test': [0]*2
    })
    received = extrapolate_2020_data(test_17, test_18)
    if not expected.equals(received):
        raise Exception('extrapolate_2020_data did not pass tests')

    # test covid_effects
    test_data = pd.DataFrame({
        'Club': ['club1', 'club2'],
        'Turnover': [100, 200],
        'Wages': [10, 20],
        'Profit before tax': [25, 50],
        'Match income': [12, 24],
        'TV and broadcasting': [45, 90],
        'Retail': np.nan*2,
        'Commercial': [150, 300],
        'Property development': [4, 8],
        'Player trading': np.nan*2,
        'Net debt': [16, 32],
        'Interest payable': [5, 10],
        'Highest paid director': [7, 14],
        'Events': [1, 2],
        'Other': [3, 6]
    })
    expected = pd.DataFrame({
        'Club': ['club1', 'club2'],
        'Turnover': [100*0.72, 200*0.72],
        'Wages': [10*0.7, 20*0.7],
        'Profit before tax': [25-35.0, 50-35.0],
        'Match income': [12*0.76, 24*0.76],
        'TV and broadcasting': [45*0.765, 90*0.765],
        'Retail': np.nan * 2,
        'Commercial': [150*0.816, 300*0.816],
        'Property development': [0.0, 0.0],
        'Player trading': np.nan * 2,
        'Net debt': [16.0, 32.0],
        'Interest payable': [5.0, 10.0],
        'Highest paid director': [7*0.7, 14*0.7],
        'Events': [0.0, 0.0],
        'Other': [3.0, 6.0]
    })
    received = covid_effects(test_data)

    if not expected.equals(received):
        raise Exception('covid_effects did not pass tests')


def import_data(file_name):
    '''
    import_data takes a file name and imports from the club_financials folder
    '''
    return pd.read_csv('data/club_financials/{}'.format(file_name))


def extrapolate_2020_data(data_17, data_18):
    '''
    extrapolate_2020_data takes data from 2017 and 2018 to predict the state
    of clubs across the league in 2020.
    Returns the 2020 predicted data
    '''
    # find mutual teams and filter so only teams in both sets are there
    mutual_teams = [val for val in data_17['Club'].tolist()
                    if val in data_18['Club'].tolist()]
    data_17 = data_17[data_17['Club'].isin(mutual_teams)].reset_index()
    data_18 = data_18[data_18['Club'].isin(mutual_teams)].reset_index()

    # find delta
    field_names = [val for val in data_18.columns if val != 'Club']
    delta_df = data_18.loc[:, field_names] - data_17.loc[:, field_names]

    # to extrapolate we need to add 2(delta) to 2018 and add clubs
    data_20 = data_18.loc[:, field_names] + (2 * delta_df)
    data_20.insert(0, 'Club', mutual_teams)
    del data_20['index']

    return data_20


def covid_effects(data_20):
    '''
    covid_effects takes the predicted 2020 data and returns the data adjusted
    for the average calcualted losses due to COVID-19.
    Returns a dataframe of predicted effects of COVID on financials in 2020
    '''
    # get the data that has information on losses due to COVID-19
    losses_df = import_data('covid_financial_loss.csv')

    # multiply percent losses to predicted 2020 data
    field_names = losses_df['Type'].tolist()
    covid_df = data_20.loc[:, field_names].multiply(
        losses_df['Percent'].tolist()
    )

    # subtract flat losses from profit
    covid_df['Profit before tax'] = data_20['Profit before tax'] - \
        losses_df.at[2, 'Flat']

    # add clubs column
    covid_df.insert(0, 'Club', data_20['Club'])

    return covid_df


def get_total_revenue():
    '''
    get_totoal_revenue writes a CSV for both predicted 2020 financials and
    predicted 2020 financials taking into account COVID-19. Function also
    writes a PNG of both to current directory.
    Returns the predicted 2020 financials of clubs due to COVID-19
    '''
    # get the data for 17, 18
    data_17 = import_data('PL_finances_16-17.csv')
    data_18 = import_data('PL_finances_17-18.csv')

    # get extrapolated 2020 data
    predicted_20 = extrapolate_2020_data(data_17, data_18)

    # save csv and make plot
    predicted_20.to_csv('predicted_financials_2020.csv')
    cols = ['Turnover', 'Wages', 'Profit before tax']
    predicted_20.plot(x='Club', y=cols, kind='bar')
    plt.title('Predicted Club Financials for 2020 (no COVID-19)')
    plt.ylabel('Amount in Euros')
    plt.savefig('predicted_financials_2020.png', bbox_inches='tight')

    # get covid predicted data based on 2020 data
    predicted_covid = covid_effects(predicted_20)

    # write covid predicted csv and png
    predicted_covid.to_csv('predicted_covid_financials_2020.csv')
    cols = ['Turnover', 'Wages', 'Profit before tax']
    predicted_covid.plot(x='Club', y=cols, kind='bar')
    plt.title('Predicted Club Financials for 2020 (with COVID-19)')
    plt.ylabel('Amount in Euros')
    plt.savefig('predicted_covid_financials_2020.png', bbox_inches='tight')

    return predicted_covid
