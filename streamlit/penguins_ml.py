import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

penguins_df = pd.read_csv('penguins.csv')
penguins_df.dropna(inplace=True)

output = penguins_df['species']

features = penguins_df[['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']]

features = pd.get_dummies(features)

output, uniques = pd.factorize(output)

X_train, x_test, Y_train, y_test = train_test_split(features, output, test_size=0.8)

rfc = RandomForestClassifier(random_state=25)
rfc.fit(X_train, Y_train)
y_pred = rfc.predict(x_test)
score = accuracy_score(y_pred, y_test)

print('The accuray score for the modle is {}'.format(score))

print('Here are the output varaibles: ')
#print(output.head())
#print('-'*75)
#print('Here are the feature variables: ')
#print(features.head())