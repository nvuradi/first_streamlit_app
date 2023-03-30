import streamlit as st
import pandas as pd
import requests as r

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
st.title("My Mom's New Healthy Diner")
st.header('Breakfast Favorites')
#st.subheader('Oatmeal')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
#st.subheader('Drinks')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
#st.subheader('Eggs')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
fruityvice_response = r.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
st.dataframe(fruits_to_show)
