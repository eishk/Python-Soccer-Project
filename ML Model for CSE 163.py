#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import pandas as pd
import csv
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import  BayesianRidge
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split



def main():
    data = pd.read_csv("data/kaggle_fifa_20/players_20.csv")
    data = shuffle(data)
    data.reset_index(inplace=True, drop=True)
    ml_models(data)
    
def ml_models(data):
    #drop more quantitative columns here
    data = data.drop(["dob", "sofifa_id", "player_url", "short_name", "long_name",
               "body_type", "player_positions", "work_rate", "player_tags", "joined", "loaned_from", 
               "player_traits", "ls", "st", "rs", "lw", "lf", "cf", "rf", "rw", "lam", "cam", "lm", "lcm",
               "cm", "ram", "rcm", "rm", "lwb", "ldm", "cdm", "rdm", "rwb", "lb", "lcb", "cb",
              "rcb", "rb"], axis = 1)
    data = data.fillna(0)
    data = data.reset_index()
    features = data.loc[:, data.columns != "value_eur"]
    features = pd.get_dummies(features)
    #this is the label I chose. I'm unsure if we chose predicting overall or market value, so I just put
    # market value. Switch if it's OVR
    labels = data["value_eur"]
    features_train, features_test, labels_train, labels_test =     train_test_split(features, labels, test_size=0.3)
    #Three ML algorithms I chose, you can add more
    model1 = LinearRegression()
    model2 = LogisticRegression()
    model3 = BayesianRidge()
    #Need some accuracy score indicator, the link below has some regression metrics.
    #https://scikit-learn.org/stable/modules/classes.html#regression-metrics
    model1.fit(features_train, labels_train)
    model2.fit(features_train, labels_train)
    model3.fit(features_train, labels_train)
    train_predictions = model1.predict(features_train)
    test_predictions = model1.predict(features_test)
    train_predictions = model2.predict(features_train)
    test_predictions = model2.predict(features_test)
    train_predictions = model3.predict(features_train)
    test_predictions = model3.predict(features_test)
    
if __name__ == '__main__':
    main()   


# In[ ]:





# In[ ]:




