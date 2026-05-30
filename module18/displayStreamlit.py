from cProfile import label

import pandas as pd
import streamlit as st
import plotly.express as px


# df = pd.DataFrame({
#     'Name' : ['Arianita', 'Festa', 'Gresa'],
#     'Age': [23, 22, 21],
#     'city': ['Prishtine', 'Prizren', 'Vushtrri']
# })
#
# df
books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.sidebar.header("Add new book data")
with st.sidebar.form("Book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author")
    new_user_rating = st.slider("User Rating", 0.0, 5.0, 0.0, 0.1)
    new_reviews = st.number_input("Reviews", min_value=0, step=1)
    new_price = st.number_input("Price", min_value=0, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Reviews': new_reviews,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_genre
    }

    books_df = pd.concat([pd.DataFrame(new_data, index=[0]), books_df], ignore_index=True)
    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index =False)
    st.sidebar.success("New book added successfully")


st.sidebar.header("Filer Options")
selected_author = st.sidebar.selectbox("Select Author", ["All"]+list(books_df['Author'].unique()))
selected_year = st.sidebar.selectbox("Select Year", ["All"]+list(books_df['Year'].unique()))
selected_Genre = st.sidebar.selectbox("Select Genre", ["All"]+list(books_df['Genre'].unique()))
min_rating = st.sidebar.slider("Minimum user rating", 0.0, 5.0, 0.0, 0.1)
max_price = st.sidebar.slider("Maximum price", 0, books_df['Price'].max(),books_df['Price'].max())




st.title("Bestselling books on amazon")
st.write("this app analyzes the amazon top selling books")

st.subheader("summary statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
avg_rating = books_df['User Rating'].mean()
avg_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("total books", total_books)
col2.metric("unique titles", unique_titles)
col3.metric("average rating", avg_rating)
col4.metric("average price", avg_price)

st.subheader("dataset preview")
st.write(books_df.head())


col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)



with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Pie Chart")
fig = px.pie(books_df, names="Genre", title="Most Liked Genre", color='Genre', color_discrete_sequence = px.colors.sequential.Plasma)
st.plotly_chart(fig)

