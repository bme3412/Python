import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv('alt_fuel_stations.csv', low_memory=False)

columns = ['Fuel Type Code', 'State', 'Latitude', 'Longitude']
df_raw = df[columns]
df_rename = df_raw.rename({'Fuel Type Code':'Fuel Type Code', 'State':'State', 'Latitude':'lat', 'Longitude':'lon'}, axis=1) 

st.title('EV Charging Infrastructure in the US')

option = st.selectbox('Which state?',('CA', 'FL', 
									  'TX', 'NV'))

st.write('You selected:', option)

df_map = df_rename[(df_rename['State']== option)]
st.map(df_map)