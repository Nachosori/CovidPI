from datetime import date
from tokenize import Name
from fastapi import APIRouter, Body, Header
from database.mongodb import db
from bson import json_util
from models.countries import Country, UpdateData, UpdateCountryName, UpdateData
from json import loads


router = APIRouter()

# Devuelve una lista de paises.

@router.get("/country")
def get_countrys():
    resul = list(db["covidpi"].find({}).distinct("country"))
    return loads(json_util.dumps(resul))

# Devuelve las coordenadas de cada país.

@router.get("/coord/{country}")
def get_coordinates(country):
    coord = list(db["covidpi"].find({"country":country}).distinct("locate"))
    return loads(json_util.dumps(coord))

# Devuelve una lista con todas las fechas disponibles

@router.get("/all/dates")
def get_all_dates():
    aux = []
    filt = {"country":"Spain"}
    project = {"_id":0, "confirmed":1}
    fechas = list(db["covidpi"].find(filt,project))
    for i in fechas[0]["confirmed"][::]:
        aux.append(i.keys())
    return loads(json_util.dumps(aux))

# Devuelve casos confirmados en un rango de tiempo.

@router.get("/confirmed/dates/{country}/{start}/{end}")
def get_coonfirmated_dates_range(country, start,end):
    start = start.replace(".", "/")
    end = end.replace(".", "/")
    filt = {"country":country}
    project = {"_id":0, "confirmed":1}
    fechas = list(db["covidpi"].find(filt,project))
    for indice in range(len(fechas[0]["confirmed"])):
        if start in list(fechas[0]["confirmed"][indice].keys()):
            start = indice
        if end in list(fechas[0]["confirmed"][indice].keys()):
            end = indice
    return loads(json_util.dumps(fechas[0]["confirmed"][start:end]))

# Devuelve casos confirmados en un dia.

@router.get("/confirmed/day/{country}/{start}")
def get_coonfirmated_dates(country, start):
    start = start.replace(".", "/")
    filt = {"country":country}
    project = {"_id":0, "confirmed":1}
    fechas = list(db["covidpi"].find(filt,project))
    for indice in range(len(fechas[0]["confirmed"])):
        if start in list(fechas[0]["confirmed"][indice].keys()):
            start = indice
    day1 = list(fechas[0]["confirmed"][start].values())
    day2 = list(fechas[0]["confirmed"][start-1].values())
    if day1[0] == 0 or day2[0] == 0:
        return day1[0]
    else:
        diference = day1[0] - day2[0]
    return loads(json_util.dumps(diference))

@router.get("/confirmed/{country}/{date}")
def get_coonfirmated(country,date):
    date = date.replace(".", "/")
    fecha = list(db["covidpi"].find({"country":country}).distinct(f"confirmed.{date}"))
    print(date)
    return loads(json_util.dumps(fecha))

@router.get("/death/dates/{country}/{start}/{end}")
def get_death_dates(country, start,end):
    start = start.replace(".", "/")
    end = end.replace(".", "/")
    filt = {"country":country}
    project = {"_id":0, "death":1}
    fechas = list(db["covidpi"].find(filt,project))
    for indice in range(len(fechas[0]["death"])):
        if start in list(fechas[0]["death"][indice].keys()):
            start = indice
        if end in list(fechas[0]["death"][indice].keys()):
            end = indice
    return loads(json_util.dumps(fechas[0]["death"][start:end]))

@router.get("/death/day/{country}/{start}")
def get_coonfirmated_dates(country, start):
    start = start.replace(".", "/")
    filt = {"country":country}
    project = {"_id":0, "death":1}
    fechas = list(db["covidpi"].find(filt,project))
    for indice in range(len(fechas[0]["death"])):
        if start in list(fechas[0]["death"][indice].keys()):
            start = indice
    day1 = list(fechas[0]["death"][start].values())
    day2 = list(fechas[0]["death"][start-1].values())
    if day1[0] == 0 or day2[0] == 0:
        return day1[0]
    else:
        diference = day1[0] - day2[0]
    return loads(json_util.dumps(diference))

@router.get("/death/{country}/{date}")
def get_death(country,date):
    date = date.replace(".", "/")
    fecha = list(db["covidpi"].find({"country":country}).distinct(f"death.{date}"))
    print(date)
    return loads(json_util.dumps(fecha))


@router.get("/recovered/dates/{country}/{start}/{end}")
def get_recovered_dates(country, start,end):
    start = start.replace(".", "/")
    end = end.replace(".", "/")
    filt = {"country":country}
    project = {"_id":0, "recovered":1}
    fechas = list(db["covidpi"].find(filt,project))
    for indice in range(len(fechas[0]["recovered"])):
        if start in list(fechas[0]["recovered"][indice].keys()):
            start = indice
        if end in list(fechas[0]["recovered"][indice].keys()):
            end = indice
    return loads(json_util.dumps(fechas[0]["recovered"][start:end]))


@router.get("/recovered/day/{country}/{start}")
def get_coonfirmated_dates(country, start):
    start = start.replace(".", "/")
    filt = {"country":country}
    project = {"_id":0, "recovered":1}
    fechas = list(db["covidpi"].find(filt,project))
    for indice in range(len(fechas[0]["recovered"])):
        if start in list(fechas[0]["recovered"][indice].keys()):
            start = indice
    day1 = list(fechas[0]["recovered"][start].values())
    day2 = list(fechas[0]["recovered"][start-1].values())
    if day1[0] == 0 or day2[0] == 0:
        return day1[0]
    else:
        diference = day1[0] - day2[0]
    return loads(json_util.dumps(diference))


@router.get("/recovered/{country}/{date}")
def get_recovered(country,date):
    date = date.replace(".", "/")
    fecha = list(db["covidpi"].find({"country":country}).distinct(f"recovered.{date}"))
    print(date)
    return loads(json_util.dumps(fecha))


# Post

@router.post("/add/country")
def add_country(country:Country):
    print(country)
    resultado = db["covidpi"].insert_one(country.dict())
    return {
        "message":"Añadido correctamente",
        "id":f"{resultado.inserted_id}"
    }

# Update

@router.put("/name/country/{name}")
def update_country(name:str,country:UpdateCountryName):
    print(country)
    db["covidpi"].update_one({ "country" : name},{ "$set": country.dict() })
    return {
        "message":"Actualizado correctamente"
        }


@router.put("/confirm/data/{name}/{date}")
def update_confirmed_number(name:str,new_date:UpdateData,date:str):
    date = date.replace(".", "/")
    date_value = list(db["covidpi"].find({"country":name}).distinct(f"confirmed.{date}"))
    new_date = new_date.dict()
    new_date = list(new_date.values())[0]
    new_date = new_date.split("-")
    new_date_dict= {new_date[0]:int(new_date[1])}
    filt = {"country":name}
    project = {"_id":0,"confirmed":1}
    list_fechas = list(db["covidpi"].find(filt,project))
    list_fechas = list_fechas[0]["confirmed"]
    index_date = list_fechas.index({date:date_value[0]})
    db["covidpi"].update_one({"country":name}, {"$set":{f"confirmed.{index_date}": new_date_dict}})
    return {
        "message":"Actualizado correctamente"
        }

@router.put("/recover/data/{name}/{date}")
def update_confirmed_number(name:str,new_date:UpdateData,date:str):
    date = date.replace(".", "/")
    date_value = list(db["covidpi"].find({"country":name}).distinct(f"recovered.{date}"))
    new_date = new_date.dict()
    new_date = list(new_date.values())[0]
    new_date = new_date.split("-")
    new_date_dict= {new_date[0]:int(new_date[1])}
    filt = {"country":name}
    project = {"_id":0,"recovered":1}
    list_fechas = list(db["covidpi"].find(filt,project))
    list_fechas = list_fechas[0]["recovered"]
    index_date = list_fechas.index({date:date_value[0]})
    db["covidpi"].update_one({"country":name}, {"$set":{f"recovered.{index_date}": new_date_dict}})
    return {
        "message":"Actualizado correctamente"
        }

@router.put("/fatal/data/{name}/{date}")
def update_confirmed_number(name:str,new_date:UpdateData,date:str):
    date = date.replace(".", "/")
    date_value = list(db["covidpi"].find({"country":name}).distinct(f"death.{date}"))
    new_date = new_date.dict()
    new_date = list(new_date.values())[0]
    new_date = new_date.split("-")
    new_date_dict= {new_date[0]:int(new_date[1])}
    filt = {"country":name}
    project = {"_id":0,"death":1}
    list_fechas = list(db["covidpi"].find(filt,project))
    list_fechas = list_fechas[0]["death"]
    index_date = list_fechas.index({date:date_value[0]})
    db["covidpi"].update_one({"country":name}, {"$set":{f"death.{index_date}": new_date_dict}})
    return {
        "message":"Actualizado correctamente"
        }

# Delete

@router.delete("/delete/country")
def add_country(country:Country):
    print(country)
    db["covidpi"].remove(country.dict())
    return {
        "message":"Eliminado correctamente"
    }