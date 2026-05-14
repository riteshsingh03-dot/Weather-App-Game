import time
import os
import requests
import msvcrt

def end():
    os.system("cls")
    print("Exiting",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    print(".",end="")
    time.sleep(0.25)
    os.system("cls")
    print("T",end="")
    time.sleep(0.15)
    print("H",end="")
    time.sleep(0.15)
    print("A",end="")
    time.sleep(0.15)
    print("N",end="")
    time.sleep(0.15)
    print("K",end=" ")
    time.sleep(0.15)
    print("Y",end="")
    time.sleep(0.15)
    print("O",end="")
    time.sleep(0.15)
    print("U",end=" ")
    time.sleep(0.15)
    print("^_^\n",end=" ")
    time.sleep(1.25)
    exit()

def mainScreen():
    os.system("cls")
    time.sleep(0.5)
    print("What do you want to do:\n")
    time.sleep(0.55)
    print("a) Know the weather of your place.")
    time.sleep(0.35)
    print("b) Guess the weather of a random place.")
    time.sleep(0.35)
    print("c) Exit\n")
    time.sleep(0.35)

    ch = msvcrt.getch().decode()
    while(ch!='a' and ch!='b' and ch!='c'):
        time.sleep(0.5)
        print("Kindly Enter a valid imput(a, b, c).")
        time.sleep(0.5)
        ch = msvcrt.getch().decode()
    
    if ch == 'c':
        time.sleep(0.25)
        end()

    if ch == 'a':
        time.sleep(0.5)
        mainCore()

def welcome():
    os.system("cls")
    time.sleep(0.5)
    print("Welcome",end=" ")
    time.sleep(0.4)
    print("to",end=" ")
    time.sleep(0.4)
    print("the",end=" ")
    time.sleep(0.4)
    print("Weather",end=" ")
    time.sleep(0.4)
    print("App",end=" ")
    time.sleep(1)
    mainScreen()

def mainCore():
    os.system("cls")
    print("Welcome to the Weather-App\n")
    time.sleep(1)
    print("Please Enter the name of the city")
    time.sleep(0.5)
    name=input("City Name: ")

    r=requests.get('https://geocoding-api.open-meteo.com/v1/search',{"name": name, "count":1})
    content = (r)
    data = (r.json())

    """"
    print("\n")
    print(r.status_code)
    print("\n")
    

    print(data)
    print("\n")
    """

    index=data["results"][0]

    print("\n\n")
    print(f"City Name: {index["name"]}")
    print(f"Latitude: {index["latitude"]}, Longitude: {index["longitude"]}")
    print(f"Elevation: {index["elevation"]}")

    #params={"longitude":index["longitude"],"latitude":index["latitude"]}

    p=requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={index["latitude"]}&longitude={index["longitude"]}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,wind_speed_10m,wind_direction_10m,rain')
    weather=p.json()
    currWeather=weather["current"]
    #print(weather)

    print("\n")
    print(f"TimeZone: {weather["timezone"]}")
    print(f"Time: {currWeather["time"]}")
    print(f"Temperature: {currWeather["temperature_2m"]} °C")
    print(f"Relative Humidity: {currWeather["relative_humidity_2m"]} %")
    print(f"Apparent Temperature: {currWeather["apparent_temperature"]} °C")
    print(f"Is_Daytime: {currWeather["is_day"]}")
    print(f"Wind Speed: {currWeather["wind_speed_10m"]} km/h")
    print(f"Wind Direction: {currWeather["wind_direction_10m"]} °")
    print(f"Rain: {currWeather["rain"]} mm")
    

mainCore()