import requests

def get_all_countries():
    return requests.get("https://covidpi.herokuapp.com/country").json()

def get_all_dates():
    return requests.get(f"https://covidpi.herokuapp.com/all/dates").json()

def get_country_coordinates(country):
    return requests.get(f"https://covidpi.herokuapp.com/coord/{country}").json()

def get_country_confirmed(country, date):
    return requests.get(f"https://covidpi.herokuapp.com/confirmed/{country}/{date}").json()

def get_country_recovered(country, date):
    return requests.get(f"https://covidpi.herokuapp.com/recovered/{country}/{date}").json()

def get_country_death(country, date):
    return requests.get(f"https://covidpi.herokuapp.com/death/{country}/{date}").json()

def get_country_confirmed_for_day(country, start):
    return requests.get(f"https://covidpi.herokuapp.com/confirmed/day/{country}/{start}").json()

def get_country_recovered_for_day(country, start):
    return requests.get(f"https://covidpi.herokuapp.com/recovered/day/{country}/{start}").json()

def get_country_death_for_day(country, start):
    return requests.get(f"https://covidpi.herokuapp.com/death/day/{country}/{start}").json()

def get_confirmated_dates_range(country, start, end):
    return requests.get(f"https://covidpi.herokuapp.com/confirmed/dates/{country}/{start}/{end}").json()

def get_recovered_dates_range(country, start, end):
    return requests.get(f"https://covidpi.herokuapp.com/recovered/dates/{country}/{start}/{end}").json()

def get_death_dates_range(country, start, end):
    return requests.get(f"https://covidpi.herokuapp.com/death/dates/{country}/{start}/{end}").json()

def post_add_countries(dict):
    return requests.post(f"https://covidpi.herokuapp.com/add/country",json=dict).json()

def upd_name_country(name,dict):
    return requests.put(f"https://covidpi.herokuapp.com/name/country/{name}",json=dict).json()

def upd_confirm_date(name,date,dict):
    return requests.put(f"https://covidpi.herokuapp.com/confirm/data/{name}/{date}",json=dict).json()

def upd_recover_date(name,date,dict):
    return requests.put(f"https://covidpi.herokuapp.com/recover/data/{name}/{date}",json=dict).json()

def upd_death_date(name,date,dict):
    return requests.put(f"https://covidpi.herokuapp.com/fatal/data/{name}/{date}",json=dict).json()

def del_delete_country(dict):
    return requests.delete(f"https://covidpi.herokuapp.com/delete/country",json=dict).json()


