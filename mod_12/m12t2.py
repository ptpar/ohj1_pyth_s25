import requests
from asetukset import apikey

#apikey = ""
#https://openweathermap.org/api
#Coordinates by
# 1. location name (esim. Helsinki)
# 2. location name and country code (esim. Helsinki,FI / Kera,FI)
# 3. paikka, maakunta, maakoodi (esim. kera,uusimaa,fi)
location = input("Enter location: ")
search_coord = f"https://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={apikey}"
try:
    response_coord = requests.get(search_coord)
    if response_coord.ok:
        response_coord_json = response_coord.json()
        if not response_coord_json:
            print("Hakusanalla ei tuloksia")
        else:
            lat = response_coord_json[0]["lat"]
            lon = response_coord_json[0]["lon"]
            search_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"
            response_weather = requests.get(search_weather).json()
            print("Weather conditions:", response_weather["weather"][0]["main"])
            print("Temperature:", round(response_weather["main"]["temp"]-273.15, 1), "celsius degrees")
    else:
        print("Hakusanalla ei tuloksia")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa")
except Exception as ex:
    print("Tapahtui odottamanton virhe:", ex)