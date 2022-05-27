import requests

def get_all_countries():
    return requests.get("http://127.0.0.1:8000/country").json()

def get_all_dates():
    return requests.get(f"http://127.0.0.1:8000/all/dates").json()

def get_country_coordinates(country):
    return requests.get(f"http://127.0.0.1:8000/coord/{country}").json()

def get_country_confirmed(country, date):
    return requests.get(f"http://127.0.0.1:8000/confirmed/{country}/{date}").json()

def get_country_recovered(country, date):
    return requests.get(f"http://127.0.0.1:8000/recovered/{country}/{date}").json()

def get_country_death(country, date):
    return requests.get(f"http://127.0.0.1:8000/death/{country}/{date}").json()

def get_country_confirmed_for_day(country, start):
    return requests.get(f"http://127.0.0.1:8000/confirmed/day/{country}/{start}").json()

def get_country_recovered_for_day(country, start):
    return requests.get(f"http://127.0.0.1:8000/recovered/day/{country}/{start}").json()

def get_country_death_for_day(country, start):
    return requests.get(f"http://127.0.0.1:8000/death/day/{country}/{start}").json()

def get_confirmated_dates_range(country, start, end):
    return requests.get(f"http://127.0.0.1:8000/confirmed/dates/{country}/{start}/{end}").json()

def get_recovered_dates_range(country, start, end):
    return requests.get(f"http://127.0.0.1:8000/recovered/dates/{country}/{start}/{end}").json()

def get_death_dates_range(country, start, end):
    return requests.get(f"http://127.0.0.1:8000/death/dates/{country}/{start}/{end}").json()

def post_add_countries(dict):
    return requests.post(f"http://127.0.0.1:8000/add/country",json=dict).json()

def upd_name_country(name,dict):
    return requests.put(f"http://127.0.0.1:8000/name/country/{name}",json=dict).json()


