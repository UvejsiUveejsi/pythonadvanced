import pandas as pd
import streamlit as st


# df = pd.DataFrame({
#     'Name' : ['Arianita', 'Festa', 'Gresa'],
#     'Age': [23, 22, 21],
#     'city': ['Prishtine', 'Prizren', 'Vushtrri']
# })
#
# df

books_df = pd.read_csv('eda-amazon-top-50-bestselling-books.ipynb')

st.title("Bestselling books on amazon")
st.write("this app analyzes the amazon top selling books")

st.subheader("summary statistics")
total_books = books_df.shape[0]
unique_titles = books_df['name']
avg_rating = books_df['user rating']
avg_price = books_df['Price']

col1, col2, col3, col4 = st.columns(4)
col1.metric("total books", total_books)
col2.metric("unique titles", unique_titles)
col3.metric("average rating", avg_rating)
col4.metric("average price", avg_price)

st.subheader("dataset preview")
st.write(books_df.head())
