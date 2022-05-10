import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Palmer's Penguins")

st.markdown('Use this app to ake your own scatterplot')

penguin_file = st.file_uploader('Select your file: ')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('penguins.csv')
    
selected_x_var = st.selectbox('Choose the x variable: ', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('Choose the y variable: ', ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g'])

fig, ax = plt.subplots()
ax = sns.scatterplot(x = penguins_df[selected_x_var],
y= penguins_df[selected_y_var], hue = penguins_df['species'])
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("scatterplot of Palmer's penguins")
st.pyplot(fig)