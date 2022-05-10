import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Palmer's penguins")
st.markdown('Make a scatterplot using streamlit')

penguin_file = st.file_uploader('Select csv file')

if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('penguins.csv')

selected_x_var = st.selectbox('Choose x variable',['bill_length_mm','bill_edpth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('Choose y variable',['bill_depth_mm','bill_length_mm', 'flipper_length_mm', 'body_mass_g'])

selected_gender = st.selectbox('Choose gender to filter',['all penguins',
'male penguins', 'female penguins'])

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass

# plot it
fig, ax  = plt.subplots()
ax = sns.scatterplot(x=penguins_df[selected_x_var],
y = penguins_df[selected_y_var], hue = penguins_df['species'])
plt.xlabel(selected_y_var)
plt.ylabel(selected_y_var)
plt.title('scatterplot of Palmer penguins: {}'.format(selected_gender))
st.pyplot(fig)