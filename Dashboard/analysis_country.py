import folium
import streamlit as st
import seaborn as sns
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

sns.set_style("whitegrid")

def analysis_country():

    countries = []

    created_list(get_all_countries(),countries)

    days =  []

    created_list(get_all_dates(),days)

    chosen_one = st.sidebar.selectbox(label="Chose a Country", options = countries)

    # Iteración de fechas.

    slider_one = st.select_slider("Select date", days, key=1)
    selector_dates = st.text(f"The chosen date is {slider_one}")

    date = slider_one.replace("/", ".")

    # Columnas de datos.

    confirmed_data = get_country_confirmed(chosen_one,date)
    recovered_data = get_country_recovered(chosen_one,date)
    death_data = get_country_death(chosen_one,date)

    confirmed_data_day = get_country_confirmed_for_day(chosen_one,date)
    recovered_data_day = get_country_recovered_for_day(chosen_one,date)
    death_data_day = get_country_death_for_day(chosen_one,date)

    # Espacio para graficas.

    dic_acu = {"Active cases": confirmed_data[0],
    "Recovered cases": recovered_data[0],
    "Death cases": death_data[0]
    }

    dic_day = {"Active cases":confirmed_data_day,
    "Recovered cases": recovered_data_day,
    "Death cases": death_data_day
    }

    selec_status = st.sidebar.radio("Covid 19 patient's status", ("For day", "Acumulated", "Date range"))

    if selec_status == "Acumulated":

        # Tabla de datos acumulados

        columns(confirmed_data[0], recovered_data[0], death_data[0], sum(death_data + recovered_data + confirmed_data))

        courses_acum = list(dic_acu.keys())
        values_acum = list(dic_acu.values())

        types_graph = ["Bar graph", "Bar pie"]

        selection_graph = st.sidebar.selectbox(label="Chose a type of graph", options = types_graph)

        if selection_graph == "Bar graph":
            st.pyplot(covid_graph(courses_acum,values_acum))
        if selection_graph == "Bar pie":
            st.pyplot(covid_pie_graf(courses_acum,values_acum))

    if selec_status == "For day":

        # Tabla de datos por dia

        columns(confirmed_data_day,recovered_data_day,death_data_day,death_data_day + recovered_data_day + confirmed_data_day)

        courses_day = list(dic_day.keys())
        values_day = list(dic_day.values())

        types_graph = ["Bar graph", "Bar pie"]

        selection_graph = st.sidebar.selectbox(label="Chose a type of graph", options = types_graph)

        if selection_graph == "Bar graph":
            st.pyplot(covid_graph(courses_day,values_day))
        if selection_graph == "Bar pie":
            st.pyplot(covid_pie_graf(courses_day,values_day))

    if selec_status == "Date range":

        days2 =  []

        created_list(get_all_dates(),days2)

        slider_one2 = st.select_slider("Select date", days2[days2.index(slider_one)+1:], key=2)
        selector_dates2 = st.text(f"The chosen date is {slider_one2}")

        date2 =slider_one2.replace("/", ".")
        
        values_range_confirmed = []
        keys_range_confirmed = []
        keys_range_recovered = []
        values_range_recovered = []
        keys_range_death = []
        values_range_death = []

        created_dict_list(get_confirmated_dates_range(chosen_one,date,date2),keys_range_confirmed,values_range_confirmed)
        created_dict_list(get_recovered_dates_range(chosen_one,date,date2),keys_range_recovered,values_range_recovered)
        created_dict_list(get_death_dates_range(chosen_one,date,date2),keys_range_death,values_range_death)


        columns(values_range_confirmed[-1] - values_range_confirmed[0], 
        values_range_recovered[-1] - values_range_recovered[0],
        values_range_death[-1] - values_range_death[0], 
        (values_range_death[-1] - (values_range_death[0]) + values_range_recovered[-1] - values_range_recovered[0]) + (values_range_confirmed[-1] - values_range_confirmed[0]))

        plt.plot(keys_range_confirmed,values_range_confirmed, '-', color="red")
        plt.plot(keys_range_confirmed, values_range_recovered, '--', color="green")
        plt.plot(keys_range_confirmed, values_range_death, color="grey")
        plt.xticks([keys_range_confirmed[0],keys_range_confirmed[-1]])
        plt.legend(["Active cases","Recovered cases", "Fatal cases"])
        

        st.pyplot(plt)

    # Localizacion de cada país.
    location = st.sidebar.checkbox("Location", False, key=3)

    if location == True:
        
        aux = get_country_coordinates(chosen_one)

        for i in aux:
            coord = i["coordinates"]

        mapa = folium.Map(coord[::], zoom_start=6)
        folium.Marker(
            coord[::],
            popup= chosen_one,
            tooltip= chosen_one
        ).add_to(mapa)
        
        st.data = st_folium(mapa, width = 725)