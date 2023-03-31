import streamlit as st
import pandas as pd
import requests as r
import snowflake.connector




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


st.header("Fruityvice Fruit Advice!")
fruit_choice=st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response = r.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#take the json response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Convert the json to df and display the df
st.dataframe(fruityvice_normalized)

#add snowflake information
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
st.text("The fruit load list contains:")
st.dataframe(my_data_row)

add_my_fruit=st.text_input('What fruit would you like do?','Jackfruit')
st.write('The user entered ', add_my_fruit)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.fruit_load_list values ('from st')");

st.stop();
