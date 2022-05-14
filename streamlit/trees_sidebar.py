import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
trees_df = pd.read_csv('trees.csv')
# add sidebar

st.title('San Francisco trees')
st.write('This app analyzes trees in San Franisco')
trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days

#st.write('The current analysis is for trees owned by: {}'.format(owners))
owners = st.sidebar.multiselect('Tree Owner Filter', trees_df['caretaker'].unique())
if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

# st.line_chart(df_dbh_grouped)

# define multiple columns
col1, col2 = st.columns(2)
with col1:
    st.write('Trees by width')
    fig_1, ax_1 = plt.subplots()
    ax_1 = sns.histplot(trees_df['dbh'])
    plt.xlabel('Tree Width')
    st.pyplot(fig_1)
with col2:
    st.write('Trees by Age')
    fig_2, ax_2 = plt.subplots()
    ax_2 = sns.histplot(trees_df['age'])
    plt.xlabel('Age, in days')
    st.pyplot(fig_2)
st.write('Trees by locattion')

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)
