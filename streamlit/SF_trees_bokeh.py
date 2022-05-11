import streamlit as st
import pandas as pd
from bokeh.plotting import figure

st.title("SF Trees")
st.write('App for trees in San Francisco')
st.subheader('using Bokeh')

trees_df = pd.read_csv('trees.csv')

scatterplot = figure(title='Bokeh scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.yaxis.axis_label = 'site_order'
scatterplot.xaxis.axis_label = 'dbh'
st.bokeh_chart(scatterplot)