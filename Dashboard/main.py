import streamlit as st
from streamlit_option_menu import option_menu
from analysis_multiple_countries import analysis_multiple_countries
from administrator_menu import administrator_menu
from analysis_country import analysis_country


# Logo y encabezado

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("https://images.squarespace-cdn.com/content/v1/5bbba6574d8711a7dcafa92a/1587756882695-3WQNYY2R1HJVFMHYQ0ET/noun_covid-19_3247096.png")

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color:#FF7F00 ;'>CovidPI</h1>", unsafe_allow_html=True)


# Menu y opciones

with st.sidebar:
    selected = option_menu(
        menu_title= None,
        options=["Home", "Analysis by Country", "Analysis by multiples countries", "Administrator menu"],
        icons=["house", "search", "archive", "lock"],
        menu_icon="cast",
        default_index=0,
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

    analysis_country()

if selected == "Analysis by multiples countries":

    analysis_multiple_countries()
    
if selected == "Administrator menu":
    
    administrator_menu()
