import streamlit as st
from bokeh.plotting import figure
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

pd.options.display.float_format = '{:,.0f}'.format
plt.style.use('fivethirtyeight')


st.set_page_config(layout="wide")
st.title("Company Data")

df = pd.read_excel('/Users/brendan/Desktop/meritech_table.xlsx')
df_edit = pd.melt(df, id_vars =['Name'], value_vars =['Equity Value', 'EV / NTM Revenue','NTM Revenue % YoY'])

company_list = list(df_edit['Name'].unique())
metric_list = list(df_edit['variable'].unique())

company = st.selectbox(label = "Choose a company", options = company_list)
metric = st.selectbox(label = "Choose a metric", options = metric_list)

query = f"Name=='{company}' & variable=='{metric}'"
df_filtered = df_edit.query(query)

metric_labels = {"Equity Value": "Market cap", "EV / NTM Revenue": "EV / NTM Revenue",'Rev Growth':'NTM Revenue % YoY'}

title = f"{metric_labels[metric]} for companies in {company}"
fig = px.line(df_filtered, x = "Name", y = "value", title = title, labels={"value": f"{metric_labels[metric]}"})
st.plotly_chart(fig, use_container_width=True)