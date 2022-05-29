import streamlit as st
import plotly as pio
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np




def created_list(function, lista):
    for i in function:
        if type(i) ==list:
            lista.append(i[0])
        else:
            lista.append(i)
    return lista

def created_dict_list(function,lista1,lista2):
    for i in function:
        auxkc = list(i.keys())
        auxvc = list(i.values())
        for i in auxkc:
            lista1.append(i)
        for i in auxvc:
            lista2.append(i)
    return lista1, lista2

def columns(*data):
    lista = ["Active cases", "Recovered cases", "Fatal cases", "Total confirmed cases" ]
    colours = ["color: red", "color: green", "color: grey", "color: #FF7F00"]
    for i, col in enumerate(st.columns(4)):
        if type[i] == list:
            with col:
                st.markdown(f"<P style='text-align: center; {colours[i]};'><b>{lista[i][0]}</b></P>", unsafe_allow_html=True)
                st.markdown(f"<P style='text-align: center; {colours[i]};'>{data[i][0]}</P>", unsafe_allow_html=True)
        else:
            with col:
                st.markdown(f"<P style='text-align: center; {colours[i]};'><b>{lista[i]}</b></P>", unsafe_allow_html=True)
                st.markdown(f"<P style='text-align: center; {colours[i]};'>{data[i]}</P>", unsafe_allow_html=True)


def radar_plot(values, name,theta):
    radar = go.Scatterpolar(
        r = values,
        theta = theta,
        name = name,
        fill = "toself"
        )
    return radar  


def covid_graph(courses,values):
    sns.set_style("whitegrid")
    plt.figure(figsize=[10,8])
    plt.bar(courses, values, width = 0.5, color=("red","green","grey"))
    plt.grid(axis='y', alpha=0.75)
    plt.ylabel("Number of cases",fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel("Number of cases",fontsize=15)
    plt.title("Dates Covid 19",fontsize=15)
    plt.show()
    return plt

def covid_pie_graf(courses,values):
    sns.set_style("whitegrid")
    labels = courses
    sizes = values
    explode = (0.1, 0, 0)  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.show()
    return plt



def covid_graph_horizon(courses,value1,value2,value3):
    sns.set_style("whitegrid")
    fig, ax = plt.subplots()
    countries = courses
    width = 0.2
    y_pos = np.arange(len(countries))
    error = np.random.rand(len(countries))
    rects1 = ax.barh(y_pos - width, value1, width, xerr=error,label="Active cases", align="center", color="red")
    rects2 = ax.barh(y_pos, value2, width, xerr=error, label="Recovered cases", align="center", color="green")
    rects3 = ax.barh(y_pos + width, value3, width, xerr=error, label="Fatal cases", align="center", color="grey")
    ax.set_yticks(y_pos, labels=countries)
    ax.invert_yaxis()
    ax.legend()
    ax.set_xlabel("Number of cases")
    ax.set_title("Dates Covid 19")
    plt.show()
    return plt


def check_password():

    def password_entered():
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        return True


