import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

st.title('San Fran trees')
st.write('This app analyzes trees in San Francisco')



trees_df = pd.read_csv('trees.csv')
trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days

# seaborn
st.subheader('using seaborn')
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age - days')
st.pyplot(fig_sb)

# matplotlib
st.subheader('using matplotlib')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'], ec='black', bins=40)
plt.xlabel('Age - days') 
st.pyplot(fig_mpl)