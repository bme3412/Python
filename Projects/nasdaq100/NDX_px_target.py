import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Nasdaq 100 Price Targets")

st.markdown('Use this Streamlit app to analyze price targets for the NDX 100')
selected_sector = st.selectbox('What sector would you like to visualize?', ['Communication Services', 'Technology','Healthcare'])
selected_x_var = st.selectbox('What sector do you want?',['Communication Services','Technology','Healthcare'])
selected_y_var = st.selectbox('What price targets?',['Low Price', 'Median Price', 'Mean Price', 'High Price', '# of Ratings', 'Avg Rating'])

# import the data
ndx_df = pd.read_csv('NDX_px_targets.csv')
ndx_df = ndx_df[ndx_df['Sector']==selected_sector]
st.write(ndx_df)

# create plots
plt.style.use('fivethirtyeight')
#markers = {'Adelie': "X", 'Gentoo':'s','Chinstrap':'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(x = ndx_df[selected_x_var],y = ndx_df[selected_y_var])
ax = sns.scatterplot(data=ndx_df, x=selected_x_var, y=selected_y_var, hue='Sector')

plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
#plt.title('Scatterplot of {} penguins'.format(selected_species))
plt.title('Scatterplot of NDX ')
st.pyplot(fig)
