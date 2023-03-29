import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.title('My Parents New Healthy Diner')
st.header('Breakfast Favorites')
#st.subheader('Oatmeal')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
#st.subheader('Drinks')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
#st.subheader('Eggs')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
