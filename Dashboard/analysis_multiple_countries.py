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

countries = []

created_list(get_all_countries(),countries)

days =  []

created_list(get_all_dates(),days)


def analysis_multiple_countries():

    selection = st.sidebar.multiselect(label="Chose a Country", options = countries)

    slider_one = st.select_slider("Select date", days, key=3)
    date = slider_one.replace("/", ".")

    list_countries = []
    list_values_confirm = []
    list_values_recovered = []
    list_values_death = []
    for country in selection:
        list_countries.append(country)
        list_values_confirm.append(get_country_confirmed(country,date)[0])
        list_values_recovered.append(get_country_recovered(country,date)[0])
        list_values_death.append(get_country_death(country,date)[0])


    # df = px.data.gapminder().query("year==2007")
    # fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
    #                    hover_name="country", size="pop",
    #                     projection="natural earth")
    # st.plotly_chart(fig)


    for i in range(len(list_values_confirm)) and range(len(list_countries)):
        st.markdown(f"<h4 style='text-align: center; color:#FF7F00 ;'>{list_countries[i]}</h4>", unsafe_allow_html=True)
        columns(list_values_confirm[i], list_values_recovered[i], list_values_death[i],(list_values_confirm[i] + list_values_recovered[i] + list_values_death[i]))


    if len(list_countries) >= 1:
        hor = covid_graph_horizon(list_countries,list_values_confirm,list_values_recovered,list_values_death)
        st.pyplot(hor)