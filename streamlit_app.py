import streamlit as st
import pandas as pd
import requests as r
import snowflake.connector
from urllib.error import URLError




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
st.dataframe(fruits_to_show)

#Create a repeatable function
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = r.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#take the json response and normalize it
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice=st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.error()

#add snowflake information
st.header("View Our Fruit List - Add Your Favorites!")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  
if st.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  my_cnx.close()
  st.dataframe(my_data_row)

#another function
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values ('"+ new_fruit +"')")
    return "Thanks for adding " + new_fruit
  
add_my_fruit=st.text_input('What fruit would you like do?')
if st.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_fn = insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  st.text(back_from_fn)




