import folium
import streamlit as st
import seaborn as sns
import time
import plotly as pio
import plotly.graph_objects as go
import plotly.express as px
from folium import Map, Marker
from streamlit_option_menu import option_menu
import numpy as np
from streamlit_folium import st_folium
import matplotlib.pyplot as plt
from data.get_data import *
from aux.func_aux import *

countries = []

created_list(get_all_countries(),countries)

days =  []

created_list(get_all_dates(),days)

def administrator_menu():

    if check_password():

        selec_options = option_menu(
        menu_title= None,
        options=["Enter data", "Change data","Deletes data"],
        icons=["geo", "search", "archive"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
        "container": {"padding": "0!important", "background-color": " #ffffff"},
        "icon": {"color": "grey", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#FF7F00"},
        "nav-link-selected": {"background-color": "#FF7F00"},
    }

        )

        if selec_options == "Enter data":
            
            title = st.text_input('Name Country')
            dic_name = {
                "country":title
            }
            if st.button("Send"):
                post_add_countries(dic_name)
                with st.spinner('Wait for it...'):
                    time.sleep(3)
                    st.success('The country has been added to the database.')

        if selec_options == "Change data":

            chosen_one = st.selectbox(label="Chose a Country", options = countries, key=1)

            selec_option = st.radio("Do you want to change the name?", ("Yes", "No"))

            if selec_option == "Yes":
                new_name = st.text_input('Change Name', key=1)
                dic_name = {
                    "country":new_name
                }
                if st.button("Send", key=1):
                    upd_name_country(chosen_one,dic_name)
                    with st.spinner('Wait for it...'):
                        time.sleep(3)
                        st.success('The name has been changed correctly.')

            if selec_option == "No":
                slider_one = st.select_slider("Select date", days, key=3)
                date = slider_one.replace("/", ".")

                confirmed_data = get_country_confirmed(chosen_one,date)
                recovered_data = get_country_recovered(chosen_one,date)
                death_data = get_country_death(chosen_one,date)

                columns(confirmed_data[0], recovered_data[0], death_data[0], death_data[0] + recovered_data[0] + confirmed_data[0])

                confirmed_number = st.text_input("Active case", key=2)
            
                dic_confirm = { "number" : slider_one+"-"+confirmed_number}
                if st.button("Send", key=2):
                    upd_confirm_date(chosen_one,date,dic_confirm)
                recovered_number = st.text_input("Recovered case", key=3)
                dic_recover = { "number" : slider_one+"-"+recovered_number}
                if st.button("Send", key=3):
                    upd_recover_date(chosen_one,date,dic_recover)
                death_number = st.text_input("Fatal case", key=3)
                dic_death = { "number" : slider_one+"-"+death_number}
                if st.button("Send",key=4):
                    upd_death_date(chosen_one,date,dic_death)
                 
        
        if selec_options == "Deletes data":

            chosen_one = st.selectbox(label="Chose a Country", options = countries, key=2)
            deleted_country = st.text_input("Type the country to delete", key=4)
            dic_delete_name = {
                "country":deleted_country
            }
            if st.button("Send", key=5):
                del_delete_country(dic_delete_name)
                with st.spinner('Wait for it...'):
                    time.sleep(3)
                    st.success('The country has been removed from the database.')

