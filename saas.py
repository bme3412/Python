import streamlit as st
from bokeh.plotting import figure
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:,.0f}'.format
plt.style.use('fivethirtyeight')

df = pd.read_excel('/Users/brendan/Desktop/meritech_table.xlsx')

df['% Price 3-Month'] = df['% Price 3-Month']* 100
df['% Price 12 Month'] = df['% Price 12 Month']*100
df['Implied ARR % YoY'] = df['Implied ARR % YoY']*100
df['LTM Revenue % YoY'] = df['LTM Revenue % YoY'] *100
df['NTM Revenue % YoY'] = df['NTM Revenue % YoY']*100
df['GM % (LTM)'] = df['GM % (LTM)']*100
df['S&M (% LTM)'] = df['S&M (% LTM)']*100
df['R&D (% LTM)'] = df['R&D (% LTM)']*100
df['G&A (% LTM)'] = df['G&A (% LTM)']*100
df['Opex (% LTM)'] = df['Opex (% LTM)']*100
df['FCF (% LTM)'] = df['FCF (% LTM)']*100
df['Rule of 40'] = df['Rule of 40']*100
df['Net Dollar Retention'] = df['Net Dollar Retention']*100

df_run = df[3:]
#df_run.plot(x='NTM Revenue % YoY',y='EV / NTM Revenue', kind='scatter')
#plt.show()


x = df_run['NTM Revenue % YoY']
y = df_run['EV / NTM Revenue']
company = df_run['Name']
size = df_run['Equity Value']
ev = df_run['Enterprise Value']
mcap = df_run['Equity Value']

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
#from bokeh.io import output_notebook
from bokeh.palettes import Viridis256 as palette
from bokeh.transform import linear_cmap
#output_notebook()

source = ColumnDataSource(
        data=dict(
            x=x,
            y=y,
            company=company,
            mcap=mcap/1000,
            size = size/1000
        )
    )
hover = HoverTool(
        tooltips=[
            ("Company", "@company"),
            ("NTM Revenue Growth % ", "$x"),
            ("EV/NTM Revenue", "$y"),
            ('Market Cap ($bn):', "@mcap")
            
        ]
    )


p = figure(plot_width=800, plot_height=800, tools=[hover],
           title="Expected Revenue Growth v EV/NTM Revenue, scaled by Market Cap")

# Defining the X-Axis Label
p.xaxis.axis_label = "NTM Revenue % YoY"
 
# defining the Y-Axis Label
p.yaxis.axis_label = 'EV / NTM Revenue'


p.circle(x='x', y='y', size='size', source=source)
show(p)

