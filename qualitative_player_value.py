'''
Authors: Eish Kapoor, Kunal Bhandarkar
Date: June 1, 2020
Desc: this file answers the question: 
What combination of qualitative variables best determines the market value of a player?
Is it age, nationality, position, overall quality, or a mixture of multiple?
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
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
    trait_features = list({
        t for trait in player_traits 
        for t in trait.split(', ')
        if '(CPU AI Only)' not in t
    })

    # modify columns for trait features, encode 1 if they have 0 if not
    for feature in trait_features:
        data[feature] = data['player_traits'].str.contains(feature).astype(int)

    return data


def build_model(data):
    '''
    build_model takes in data and trains a model on an 80% testing sample.
    Returns a dictionary with the mapping:
    {'model': model, 'training_accuracy': score, 'training_accuracy': score,
    'features': features_list, 'label': label_name}
    '''
    # get the features and labels from data
    feature_mask = (data.columns != 'player_traits') & \
        (data.columns != 'value_eur')
    features = data.loc[:, feature_mask]
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
    Returns a dictionary of the model and it's accuracy score on test
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
    
    return model_info