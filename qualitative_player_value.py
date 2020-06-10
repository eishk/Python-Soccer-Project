'''
Authors: Eish Kapoor, Kunal Bhandarkar
Date: June 1, 2020
Desc: this file answers the question:
What combination of qualitative variables best determines the market value of a
player?
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import os


def test_cleaning():
    '''
    test_cleaning is a test function to make sure that the data is clean and
    properly formatted before being fed to the model
    raises an exception if it finds an error
    '''
    # write csv data for import_csv to read
    test_data = pd.DataFrame({
        'value_eur': [123000, 234000],
        'player_traits': ['asdf, qwer, zxcv', 'qwer, jkl'],
        'extra': [123, 234],
        'more extra': [923, 9123]
    })
    test_data.to_csv('test_tmp.csv')

    # get expected and received values
    expected = pd.DataFrame({
        'value_eur': [123000, 234000],
        'jkl': [0, 1],
        'asdf': [1, 0],
        'qwer': [1, 1],
        'zxcv': [1, 0],
    })
    expected = expected.reindex(sorted(expected.columns), axis=1)
    received = import_csv('../../test_tmp.csv')
    received = received.reindex(sorted(received.columns), axis=1)

    if not received.equals(expected):
        raise Exception('import_csv did not pass tests')

    # clean extra file
    os.remove('test_tmp.csv')


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
    trait_features = list({
        t for trait in player_traits
        for t in trait.split(', ')
        if '(CPU AI Only)' not in t
    })

    # modify columns for trait features, encode 1 if they have 0 if not
    for feature in trait_features:
        data[feature] = data['player_traits'].str.contains(feature).astype(int)
    del data['player_traits']

    return data


def build_model(data):
    '''
    build_model takes in data and trains a model on an 80% testing sample.
    Returns a dictionary with the mapping:
    {'model': model, 'training_accuracy': score, 'training_accuracy': score,
    'features': features_list, 'label': label_name}
    '''
    # get the features and labels from data
    features = data.loc[:, data.columns != 'value_eur']
    labels = data['value_eur']

    # split data into test and training
    features_train, features_test, label_train, label_test = \
        train_test_split(features, labels, test_size=0.2, random_state=1)

    # create a regression model and train it
    model = DecisionTreeRegressor()
    model.fit(features_train, label_train)

    # package model, training, and test accuracy
    package = {
        'model': model,
        'training_score': model.score(features_train, label_train),
        'test_score': model.score(features_test, label_test),
        'features': features.columns,
        'label': 'value_eur'
    }

    return package


def plot_model(model_info):
    '''
    plot_model takes in a DecisionTreeRegressor model and creates and saves
    a visualization to this directory under regressor_tree.png and a visual
    of the most important features to the model under tree_importance.png
    '''
    model = model_info['model']

    # save visualization for the tree (expensive process)
    fig, _ = plt.subplots(nrows=1, ncols=1)
    tree.plot_tree(model)
    fig.savefig('regressor_tree.png')

    # visualization for feature importance
    fig, _ = plt.subplots(nrows=1, ncols=1)
    heights = model.feature_importances_
    features = model_info['features']
    y_pos = np.arange(len(features))
    plt.bar(y_pos, heights)
    plt.xticks(y_pos, features, rotation=90)
    plt.tight_layout()
    plt.ylabel('Percent Importance')
    plt.title('Importance vs Feature in Regressor Model')
    plt.savefig('tree_importance.png', bbox_inches='tight')


def get_qualitative_value():
    '''
    get_qualitative_value() cleans data and trains a model to predict
    qualitative geatures that result in a player's value.
    prints information about the model and it's accuracy score on test
    and training data
    Saves a visualization of the model and it's most important features
    to current directory.
    '''
    # import, clean, and prepare csv data for ML model
    data = import_csv('players_20.csv')

    # build model and store information about it
    model_info = build_model(data)

    # plot model information
    plot_model(model_info)

    # print basic information about model
    print('model features:', model_info['features'])
    print('model label:', model_info['label'])
    print('model accuracy score:', model_info['training_score'])
