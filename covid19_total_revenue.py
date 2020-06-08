'''
Authors: Eish Kapoor, Kunal Bhandarkar
Date: June 1, 2020
Desc: this file answers the question: 
What will the effect of COVID-19 be on the total revenue of the Premier League?
'''

import pandas as pd
import matplotlib as plt


def import_data(file_name):
    '''
    import_data takes a file name and imports it from the data/club_financials folder
    '''
    return pd.read_csv('data/club_financials/{}'.format(file_name))


def extrapolate_2020_data(data_17, data_18):
    '''
    extrapolate_2020_data takes data from 2017 and 2018 to predict the state of clubs across 
    the league in 2020. Writes a csv to the current directory with the information in addition
    to a png plot. Returns the 2020 predicted data
    '''

    # find mutual teams and filter so data so that only teams that are in both sets are there
    mutual_teams = [val for val in data_17['Club'].tolist() if val in data_18['Club'].tolist()]
    data_17 = data_17[data_17['Club'].isin(mutual_teams)].reset_index()
    data_18 = data_18[data_18['Club'].isin(mutual_teams)].reset_index()

    # find delta
    field_names = [val for val in data_18.columns if val != 'Club']
    delta_df = data_18.loc[:, field_names] - data_18.loc[:, field_names]

    # to extrapolate we need to add 2(delta) to 2018 and add clubs
    data_20 = data_18.loc[:, field_names] + (2 * delta_df)
    data_20.insert(0, 'Club', mutual_teams)

    # save csv and make plot
    data_20.to_csv('predicted_financials_2020.csv')
    tmp = pd.DataFrame({'Turnover': data_20['Turnover'], 'Wages': data_20['Wages'], 'Profit': data_20['Profit before tax']}, index=data_20['Club'])
    ax = tmp.plot.bar(rot=0)
    ax.figure.savefig('predicted_financials_2020.png')

    return data_20

    
def covid_effects(data_20):
    '''
    covid_effects takes the predicted 2020 data and returns the data adjusted for the average
    calcualted losses due to COVID-19. Writes a csv to the current directory and a png of the 
    plot of basic stats. Returns a dataframe of predicted effects of COVID on financials in 2020
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

    # write csv and plot
    covid_df.to_csv('predicted_covid_financials_2020.csv')
    tmp = pd.DataFrame({'Turnover': covid_df['Turnover'], 'Wages': covid_df['Wages'], 'Profit': covid_df['Profit before tax']}, index=covid_df['Club'])
    ax = tmp.plot.bar(rot=0)
    ax.figure.savefig('predicted_covid_financials_2020.png')

    return covid_df


def get_total_revenue():
    '''
    get_totoal_revenue writes a CSV for both predicted 2020 financials and predicted 2020 financials
    taking into account COVID-19. Function also writes a PNG of both to current directory. Returns
    the predicted 2020 financials of clubs due to COVID-19
    '''
    # get the data for 17, 18
    data_17 = import_data('PL_finances_16-17.csv')
    data_18 = import_data('PL_finances_17-18.csv')

    # get extrapolated 2020 data
    predicted_20 = extrapolate_2020_data(data_17, data_18)

    # get covid predicted data based on 2020 data
    predicted_covid = covid_effects(predicted_20)

    return predicted_covid
get_total_revenue()