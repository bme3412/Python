import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt
st.title('Analyzing my Goodreads')
st.subheader('A Web App by [Brendan Erhard]')

goodreads_file = st.file_uploader('Please import your data')
if goodreads_file is None:
    books_df = pd.read_csv('goodreads_library_export.csv')
    st.write('Analyzing Brendan"s reading history')
else:
    books_df = pd.read_csv(goodreads_file)
    st.write('Analyzing Brendan"s reading history')

books_df['Year Finished'] = pd.to_datetime(books_df['Date Read']).dt.year
books_per_year = books_df.groupby('Year Finished')['Book Id'].count().reset_index()
books_per_year.columns = ['Year Finished', 'Count']
fig_year_finished = px.bar(books_per_year, x='Year Finished', y='Count')
st.plotly_chart(fig_year_finished)

# How long to take a book that started?
books_df['days_to_finish'] = (pd.to_datetime(books_df['Date Read']) - pd.to_datetime(books_df['Date Added'])).dt.days
books_finished_filtered = books_df[(books_df['Exclusive Shelf'] =='read') & (books_df['days_to_finish'] >= 0)]
fig_days_finished = px.histogram(books_finished_filtered, x='days_to_finish', title='Time Between date added and date finished', labels={'days_to_finish': 'days'})
st.plotly_chart(fig_days_finished)

# How long are the books that I have read?
fig_num_pages = px.histogram(books_df, x='Number of Pages', title='Book Length Histogram')
st.plotly_chart(fig_num_pages)

# How old ate the books that I have read?
st.write('Assumption check')
st.write(len(books_df[books_df['Original Publication Year'] > books_df['Year Published']]))

books_publication_year = books_df.groupby('Original Publication Year')['Book Id'].count().reset_index()
books_publication_year.columns = ['Year Published', 'Count']
fig_year_published = px.bar(books_publication_year, x='Year Published', y='Count', title='Book Age Plot')
st.plotly_chart(fig_year_published)