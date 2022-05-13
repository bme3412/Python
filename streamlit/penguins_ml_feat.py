import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
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

print('The accuracy score for the model is {}'.format(score))
rf_pickle = open('random_forest_penguin.pickle', 'wb')
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open('output_penguin.pickle', 'wb')
pickle.dump(uniques, output_pickle)
output_pickle.close()

#print('Here are the output variables: ')
#print(output.head())
#print('-'*75)
#print('Here are the feature variables: ')
#print(features.head())

rf_pickle = open('random_forest_penguin.pickle', 'rb')
map_pickle = open('output_penguin.pickle', 'rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
st.write(rfc)
st.write(unique_penguin_mapping)

fig, ax = plt.subplots()
ax = sns.barplot(rfc.feature_importances_,features.columns)
plt.title('Which features are the most important for species prediction?')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
fig.savefig('feature_importance.png')

st.title('Penguin Classifier')
st.write('This app uses 6 inputs to predict the species of penguin: ')
rf_pickle = open('random_forest_penguin.pickle', 'rb')
map_pickle = open('output_penguin.pickle', 'rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()

island = st.selectbox('Penguin Island', options=['Biscoe', 'Dream', 'Torgerson'])
sex = st.selectbox('Sex', options=['Female', 'Male'])
bill_length = st.number_input('BIll length', min_value=0)
bill_depth = st.number_input('Bill depth', min_value=0)
flipper_length = st.number_input('Flipper length', min_value=0)
body_mass = st.number_input('Body mass', min_value=0)
island_briscoe, island_dream, island_torgerson = 0, 0, 0
if island == 'Briscoe':
    island_briscoe =1
elif island == 'Dream':
    island_dream = 1
elif island == 'Torgerson':
    island_torgerson = 1

sex_female, sex_male = 0,0
if sex == 'Female':
    sex_female = 1
elif sex == 'Male':
    sex_male =1

# run the prediction
new_prediciton = rfc.predict([[bill_length, bill_depth, flipper_length, body_mass, island_briscoe, island_dream, island_torgerson, sex_female, sex_male]])
prediction_species = unique_penguin_mapping[new_prediciton][0]
st.write('We predict your penguin is of the {} species'.format(prediction_species))
st.image('feature_importance.png')

st.write('Below are the histograms for each continuous variable '
         'separated by penguin species. The vertical line '
         'represents your the inputted value.')

fig, ax = plt.subplots()
ax = sns.displot(x=penguins_df['bill_length_mm'], hue=penguins_df['species'])
plt.axvline(bill_length)
plt.title("Bill Length by species")
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguins_df['bill_depth_mm'], hue=penguins_df['species'])
plt.axvline(bill_depth)
plt.title('Bill Depth by species')
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguins_df['flipper_length_mm'], hue=penguins_df['species'])
plt.axvline(flipper_length)
plt.title('Flipper Length by species')
st.pyplot(ax)