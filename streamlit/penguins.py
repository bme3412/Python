import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Palmer's Penguins")



st.markdown('Use this Streamlit app to make your own scatterplot about penguins')
#selected_species = st.selectbox('What species would you like to visualize?', ['Adelie', 'Gentoo','Chinstrap'])
selected_x_var = st.selectbox('What do you want x variable to be?',['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('What about y?',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

# import the data
penguins_df = pd.read_csv('penguins.csv')
#penguins_df = penguins_df[penguins_df['species']==selected_species]

# create plots
plt.style.use('fivethirtyeight')
markers = {'Adelie': "X", 'Gentoo':'s','Chinstrap':'o'}
fig, ax = plt.subplots()
#ax = sns.scatterplot(x = penguins_df[selected_x_var],y = penguins_df[selected_y_var])
ax = sns.scatterplot(data=penguins_df, x=selected_x_var, y=selected_y_var, hue='species', markers=markers,style='species')

plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
#plt.title('Scatterplot of {} penguins'.format(selected_species))
plt.title('Scatterplot of Palmer penguins')
st.pyplot(fig)