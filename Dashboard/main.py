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
from aux.func_aux import check_password, columns, covid_graph, covid_graph_horizon, created_dict_list, created_list
from data.get_data import  * 

# Logo y encabezado

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("https://images.squarespace-cdn.com/content/v1/5bbba6574d8711a7dcafa92a/1587756882695-3WQNYY2R1HJVFMHYQ0ET/noun_covid-19_3247096.png")

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color:#FF7F00 ;'>CovidPI</h1>", unsafe_allow_html=True)

countries = []

created_list(get_all_countries(),countries)

days =  []

created_list(get_all_dates(),days)

# Menu y opciones

with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options=["Home", "Analysis by Country", "Analysis by multiples countries", "Administrator menu"],
        icons=["house", "search", "archive", "lock"],
        menu_icon="cast",
        default_index=2,
        styles={
        "container": {"padding": "0!important", "background-color": " #f3f3f3"},
        "icon": {"color": "grey", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#FF7F00"},
        "nav-link-selected": {"background-color": "#FF7F00"},
    }

        )  

if selected == "Home":
    st.markdown(f"<h2 style='text-align: center; color: grey;'>Directions</h2>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color: #566573;'>The CovidPi API will show you different interactive maps and graphs that describe the geographical spread of the virus around the world. </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color: #566573;'>We aggregate data from the following database: </h5>", unsafe_allow_html=True)
    st.markdown(f"<a href=https://www.kaggle.com/datasets/baguspurnama/covid-confirmed-global rel='nofollow; '>Data Covid-19 Global</a>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color: #566573;'>To start choose the category in the sidebar. &#x1f448 </h5>", unsafe_allow_html=True)

if selected == "Analysis by Country":

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

        st.pyplot(covid_graph(courses_acum,values_acum))

    if selec_status == "For day":

        # Tabla de datos por dia

        columns(confirmed_data_day,recovered_data_day,death_data_day,death_data_day + recovered_data_day + confirmed_data_day)

        courses_day = list(dic_day.keys())
        values_day = list(dic_day.values())

        st.pyplot(covid_graph(courses_day,values_day))

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

if selected == "Analysis by multiples countries":
    
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

    
    for i in range(len(list_values_confirm)):
        columns(list_values_confirm[i], list_values_recovered[i], list_values_death[i],(list_values_confirm[i] + list_values_recovered[i] + list_values_death[i]))


    if len(list_countries) >= 1:
        hor = covid_graph_horizon(list_countries,list_values_confirm,list_values_recovered,list_values_death)
        st.pyplot(hor)

if selected == "Administrator menu":

    if check_password():

        selec_options = option_menu(
        menu_title= None,
        options=["Enter data", "Change data","Deletes data"],
        icons=["geo", "search", "archive"],
        menu_icon="cast",
        default_index=2,
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

        if selec_options == "Change data":

            chosen_one = st.selectbox(label="Chose a Country", options = countries)

            selec_option = st.radio("Do you want to change the name?", ("Yes", "No"))

            if selec_option == "Yes":
                new_name = st.text_input('Change Name')
                dic_name = {
                    "country":new_name
                }
                if st.button("Send"):
                    upd_name_country(chosen_one,dic_name)

            if selec_option == "No":
                slider_one = st.select_slider("Select date", days, key=3)
                date = slider_one.replace("/", ".")

                confirmed_data = get_country_confirmed(chosen_one,date)
                recovered_data = get_country_recovered(chosen_one,date)
                death_data = get_country_death(chosen_one,date)

                columns(confirmed_data[0], recovered_data[0], death_data[0], sum(death_data + recovered_data + confirmed_data))

                confirmed = st.text_input("Active case", key=1)
                #  if st.button("Send"):
                recoverd = st.text_input("Recovered case", key=2)
                #  if st.button("Send"):
                death = st.text_input("Fatal case", key=3)
                #  if st.button("Send"):


