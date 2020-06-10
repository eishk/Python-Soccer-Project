"""
Eish Kapoor & Kunal Bhandarkar
CSE 163 AD
Final Project

This file contains the code that analyzes the scraped data
from the TransferMarkt and the earlier results from question 1
to answer the question of part 2 relating to how much will clubs
pay for the same quality.
"""
import matplotlib.pyplot as plt
import pandas as pd
from math import isclose


def main_analysis():
    dataset_2017 = merged_2017_data()
    dataset_2020 = merged_2020_data()
    cost_per_ovr_2017 = data_analysis(dataset_2017, "2017")
    cost_per_ovr_2020 = data_analysis(dataset_2020, "2020")
    financial_analysis(cost_per_ovr_2017, cost_per_ovr_2020)


def merged_2017_data():
    """
    Takes data from the two scraped files from 2017- transfers and players
    value- and merges them together with the fifa dataset. Returns the merged
    dataset of the players that were transferred in and out of the Premier
    League with their stats and ratings from FIFA 17. Also creates csv version
    of returned file.
    """
    premier_league_2017 = ['Arsenal', 'Bournemouth', 'Burnley', 'Chelsea',
                           'Crystal Palace', 'Everton', 'Leicester City',
                           'Liverpool', 'Manchester City', 'Manchester United',
                           'Southampton', 'Stoke City', 'Swansea City',
                           'Tottenham Hotspur', 'Watford',
                           'West Bromwich Albion', 'West Ham United',
                           'Hull City', 'Middlesbrough', 'Sunderland']
    fifa_data = pd.read_csv('data/kaggle_fifa_20/players_17.csv')
    transfer_data = pd.read_csv('data/transfer_data/transfers_2017.csv')
    value_data = pd.read_csv('data/player_value/playersvalue_2017.csv')
    premier_league = (fifa_data["club"].isin(premier_league_2017))
    fifa_data = fifa_data[premier_league]
    # Because the way names are formatted is different in the FIFA dataset and
    # the scraped dataset, we had to reformat in order to do a successful join.
    transfer_data['first name'] = transfer_data.Name.str.split(' ').str[0]
    transfer_data['last name'] = transfer_data.Name.str.split(' ').str[1]
    transfer_data['first initial'] = transfer_data['first name'].str[0] + ". "
    transfer_data["Short Name"] = transfer_data['first initial']
    + transfer_data['last name']
    merged_scrape_data = transfer_data.merge(value_data, left_on='Name',
                                             right_on='Name', how='inner')
    merged_scrape_data.sort_values("Name", inplace=True)
    merged_scrape_data.drop_duplicates(subset="Name",
                                       keep=False, inplace=True)
    initial = fifa_data.merge(merged_scrape_data, left_on='short_name',
                              right_on='Short Name', how='inner')
    first_name = fifa_data.merge(merged_scrape_data, left_on='short_name',
                                 right_on='first name', how='inner')
    last_name = fifa_data.merge(merged_scrape_data, left_on='short_name',
                                right_on='last name', how='inner')
    name = fifa_data.merge(merged_scrape_data, left_on='short_name',
                           right_on='Name', how='inner')
    frames = [initial, first_name, last_name, name]
    result = pd.concat(frames)
    result.sort_values("long_name", inplace=True)
    result.drop_duplicates(subset="long_name",
                           keep=False, inplace=True)
    result = result[result["Actual Fee"] != 0]
    result = result[result["short_name"] != "Coutinho"]
    result.to_csv('ultimate_file_2017.csv', encoding='utf-8')
    return result


def merged_2020_data():
    """
    Takes data from the two scraped files from 2017- transfers and players
    value- and merges them together with the fifa dataset. Returns the merged
    dataset of the players that were transferred in and out of the Premier
    League with their stats and ratings from FIFA 17. Also creates csv version
    of returned file.
    """
    premier_league_2020 = ['Arsenal', 'Aston Villa', 'Bournemouth',
                           'Brighton & Hove Albion', 'Burnley', 'Chelsea',
                           'Crystal Palace', 'Everton', 'Leicester City',
                           'Liverpool', 'Manchester City', 'Manchester United',
                           'Newcastle United', 'Norwich City', 'Southampton',
                           'Sheffield United', 'Tottenham Hotspur', 'Watford',
                           'West Ham United', 'Wolverhampton Wanderers']
    fifa_data = pd.read_csv('data/kaggle_fifa_20/players_20.csv')
    transfer_data = pd.read_csv('data/transfer_data/transfers_2020.csv')
    value_data = pd.read_csv('data/player_value/playersvalue_2020.csv')
    premier_league = (fifa_data["club"].isin(premier_league_2020))
    fifa_data = fifa_data[premier_league]
    # Because the way names are formatted is different in the FIFA dataset and
    # the scraped dataset, we had to reformat in order to do a successful join.
    transfer_data['first name'] = transfer_data.Name.str.split(' ').str[0]
    transfer_data['last name'] = transfer_data.Name.str.split(' ').str[1]
    transfer_data['first initial'] = transfer_data['first name'].str[0] + ". "
    transfer_data["Short Name"] = transfer_data['first initial']
    + transfer_data['last name']
    merged_scrape_data = transfer_data.merge(value_data, left_on='Name',
                                             right_on='Name', how='inner')
    merged_scrape_data.sort_values("Name", inplace=True)
    merged_scrape_data.drop_duplicates(subset="Name",
                                       keep=False, inplace=True)
    initial = fifa_data.merge(merged_scrape_data, left_on='short_name',
                              right_on='Short Name', how='inner')
    first_name = fifa_data.merge(merged_scrape_data, left_on='short_name',
                                 right_on='first name', how='inner')
    last_name = fifa_data.merge(merged_scrape_data, left_on='short_name',
                                right_on='last name', how='inner')
    name = fifa_data.merge(merged_scrape_data, left_on='short_name',
                           right_on='Name', how='inner')
    frames = [initial, first_name, last_name, name]
    result = pd.concat(frames)
    result.sort_values("long_name", inplace=True)
    result.drop_duplicates(subset="long_name",
                           keep=False, inplace=True)
    result = result[result["Actual Fee"] != 0]
    result.to_csv('ultimate_file_2020.csv', encoding='utf-8')
    return result


def data_analysis(data, year):
    """
    Takes given dataset and prints some important facts about the
    data that are necessary for understanding the growth in soccer.
    Also in the data analysis, computes and returns the cost per overall
    in the British Premier League for that season(the season the dataset
    represents).
    """
    mean_ovr = data['overall'].mean()
    mean_fee = data['Actual Fee'].mean()
    print("In " + year +
          ", the average overall rating of the players transferred" +
          " was " + str(mean_ovr) + ", with the average fee paid of "
          + str(mean_fee) + " euros.")
    cost_per_ovr = mean_fee / mean_ovr
    print("The cost a Premier League club on average for every extra overall"
          + " rating of a" + " player(overall determined by FIFA) was " +
          str(cost_per_ovr) + " euros.")
    return cost_per_ovr


def financial_analysis(cpo_2017, cpo_2020):
    """
    Takes the cost per overall for both years and processes data from the
    financial csvs from part 1 to reveal the effect of COVID on the cost per
    overall, and thus the transfer market.
    """
    growth_of_cost = (cpo_2020 - cpo_2017) / 3
    finance_data_17 = pd.read_csv('data/club_financials/PL_finances_16-17.csv')
    finance_data_18 = pd.read_csv('data/club_financials/PL_finances_17-18.csv')
    turnover_2017 = finance_data_17["Turnover"].mean()
    turnover_2018 = finance_data_18["Turnover"].mean()
    print("The average turnover/revenue for a Premier League club in 2017 was "
          + str(turnover_2017*1000000) + " euros, while in 2018 it was "
          + str(turnover_2018*1000000) + " euros.")
    growth_of_turnover = (turnover_2018 - turnover_2017)
    percent_growth_in_turnover = growth_of_turnover / turnover_2017
    turnover_2020 = turnover_2018 + (2 * growth_of_turnover)
    print("Using the change from the 2017 to the 2018 season, we estimated" +
          " the average revenue for the" +
          " 2020 season using linear growth and got the estimate of " +
          str(turnover_2020 * 1000000) + " million euros " +
          "per club without the effect of corona.")
    percent_growth_in_cpo = growth_of_cost / cpo_2017
    print(" The percentage growth in cost per overall from the 2017" +
          " to the 2020 season was " + str(percent_growth_in_cpo*100) + "%.")
    print(" The percentage growth in revenue/turnover from the 2017" +
          " to the 2020 season was " +
          str(percent_growth_in_turnover*100) + "%.")
    cost_turnover_ratio = percent_growth_in_cpo/percent_growth_in_turnover
    print("For every 1% change in turnover, there is a " +
          str(cost_turnover_ratio) + "% change in cost per overall.")
    pred_financials = pd.read_csv('predicted_financials_2020.csv')
    pred_covid_finances = pd.read_csv('predicted_covid_financials_2020.csv')
    predicted_mean = pred_financials["Turnover"].mean()
    covid_mean = pred_covid_finances["Turnover"].mean()
    change_in_spending_power = (((covid_mean - predicted_mean)/predicted_mean)
                                + .25)*cost_turnover_ratio
    change_in_spending_power = abs(change_in_spending_power)
    print("With our estimated effect of coronavirus on" +
          " the financials of the Premier League" +
          " clubs, we found the percentage change in turnover " +
          "from what was predicted for 2020, and adjusted that " +
          "for the loan being given to each Premier League clubs that" +
          " is 25% of their expected revenue. This is then multiplied by " +
          "the multiplier we found that signifies the relationship" +
          " between cost per overall and turnover. This gives us the" +
          " change in spending power.")
    print("The change in spending power is a decrease of " +
          str(change_in_spending_power*100) + " percent.")
    new_avr_per_ovr_2020 = cpo_2020 * (1-change_in_spending_power)
    print("With this change in spending power, the new average "
          + "cost per overall is " + str(new_avr_per_ovr_2020) + " euros.")
    cost_per_ovr_plot(cpo_2017, cpo_2020, new_avr_per_ovr_2020)


def cost_per_ovr_plot(cpo_2017, cpo_2020, cpo_2020_covid):
    """
    Creates the bar plot showing the differences in the cost per overall point
    in the Premier League and the predicted cost per overall point.
    """
    fig, ax = plt.subplots(1, 1, tight_layout=True)
    years = ['2017', '2020 Without Covid', '2020 With Covid']
    cpo = [cpo_2017, cpo_2020, cpo_2020_covid]
    ax.bar(years, cpo)
    plt.title("Premier League's Cost Per FIFA Overall Point")
    plt.xlabel('Past & Predicted Years')
    plt.ylabel('Euros per Overall')
    plt.savefig('cpo_thru_the_years.png')


def test_cpo(cpo_2017, cpo_2020):
    """
    Test function to check whether the cost per overall for each year
    is correct. Throws exception detailing problem if not.
    """
    correct_cpo_2017 = 103029.04564315354
    if not isclose(cpo_2017, correct_cpo_2017):
        raise Exception('Cost Per Overall 2017 is wrong. Did not pass tests.')
    correct_cpo_2020 = 339261.1683848797
    if not isclose(cpo_2020, correct_cpo_2020):
        raise Exception('Cost Per Overall 2020 is wrong. Did not pass tests.')


def test_dataset(dataset_2017, dataset_2020):
    """
    Test function to determine whether the dataset merging and filtering
    functions are correct. Throws exception detailing problem if not.
    """
    mean_ovr_2017 = dataset_2017['overall'].mean()
    mean_fee_2017 = dataset_2017['Actual Fee'].mean()
    correct_mean_ovr_2017 = 80.33
    correct_mean_fee_2017 = 8276666.66
    if not isclose(mean_ovr_2017, correct_mean_ovr_2017):
        raise Exception('2017 Dataset mean overall is wrong.'
                        'Did not pass tests.')
    if not isclose(mean_fee_2017, correct_mean_fee_2017):
        raise Exception('2017 Dataset mean fee is wrong.'
                        'Did not pass tests.')
    mean_ovr_2020 = dataset_2020['overall'].mean()
    mean_fee_2020 = dataset_2020['Actual Fee'].mean()
    correct_mean_ovr_2020 = 72.75
    correct_mean_fee_2020 = 24681250
    if not isclose(mean_ovr_2020, correct_mean_ovr_2020):
        raise Exception('2020 Dataset mean overall is wrong.'
                        'Did not pass tests.')
    if not isclose(mean_fee_2020, correct_mean_fee_2020):
        raise Exception('2020 Dataset mean fee is wrong.'
                        'Did not pass tests.')
