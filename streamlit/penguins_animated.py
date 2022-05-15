from importlib_metadata import re
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_penguin = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json')
st_lottie(lottie_penguin, speed=1.5,width=800, height=400)

st.title("Palmer's Penguins")
st.markdown('Use this streamlit app to make a scatterplot')

selected_x_var = st.selectbox('Choose x variable',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('Choose y', ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g'])

penguin_file = st.file_uploader('Select csv file')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('penguins.csv')
plt.style.use('fivethirtyeight')
markers = {'Adelie':'X', 'Gentoo':'s', 'Chinstrap':'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data=penguins_df, x=selected_x_var, y=selected_y_var, hue='species', markers=markers,style='species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title('Scatterplot of penguins')
st.pyplot(fig)