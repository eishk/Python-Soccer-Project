'''
Authors: Eish Kapoor, Kunal Bhandarkar
Date: June 1, 2020
Desc: this file answers the question: 
What combination of qualitative variables best determines the market value of a player?
Is it age, nationality, position, overall quality, or a mixture of multiple?
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor


def import_csv(file_name):
    '''
    import_csv reads a csv from data/kaggle_fifa_20 folder then cleans and
    returns it
    '''
    data = pd.read_csv('data/kaggle_fifa_20/{}'.format(file_name))
    
    # get the features that we want to analyze
    features = ['value_eur', 'player_traits']
    data = data[features].dropna()

    # parse player_traits and create new feature columns
    player_traits = data['player_traits'].tolist()
    trait_features = {
        t for trait in player_traits 
        for t in trait.split(', ')
        if '(CPU AI Only)' not in t
    }

    # modify columns for trait features
    data.drop(columns=['player_traits'])

    return data


def build_model(data):
    '''
    build_model does something cool
    '''
    features = data['player_traits']
    labels = data['value_eur']
    features_train, features_test, label_train, label_test = \
        train_test_split(data['value'])


def get_qualitative_value():
    '''
    This is a temporary function
    '''
    data = import_csv('players_20.csv')  # import 2020 player FIFA data



get_qualitative_value()