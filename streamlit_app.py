import streamlit
import pandas as pd

streamlit.title('My Parents New Healty Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')

# Lets put a pick list here so they can pick a the fruit they wnat to incluide
streamlit.multiselect("Pick some fruits:", list(fruit_list.index),['Avocado', 'Strawberries'])
#display the table on the page
streamlit.dataframe(fruit_list)