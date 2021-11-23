import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('BigMac Index')

@st.cache
def load_data():
    data = pd.read_csv('bigmac.csv')
    return data.assign(data = lambda d: pd.to_datetime(d['date']))

df = load_data()

# select countries
countries = st.sidebar.multiselect(
    "Select Countries",
    df['name'].unique()
)

varname = st.sidebar.selectbox(
    "Select column",
    ("local_price", "dollar_price")
)

subset_df = df.loc[lambda d: d['name'].isin(countries)]

for name in countries:
    plotset = subset_df.loc[lambda d: d['name'] == name]
    plt.plot(plotset['date'], plotset[varname], label=name)
plt.legend()
st.pyplot()

if st.sidebar.checkbox("Show Raw Data"):
    st.markdown("### Raw Data")
    st.write(subset_df)