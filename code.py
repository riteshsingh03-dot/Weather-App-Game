import time
import os
import requests
import msvcrt
import random

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
    print("Welcome!\n")
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

    if ch == 'b':
        time.sleep(0.5)
        gameCore()

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

    os.system("cls")
    print(f"City Name: {index["name"]}")
    time.sleep(0.35)
    print(f"Latitude: {index["latitude"]}, Longitude: {index["longitude"]}")
    time.sleep(0.35)
    print(f"Elevation: {index["elevation"]}")

    #params={"longitude":index["longitude"],"latitude":index["latitude"]}

    p=requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={index["latitude"]}&longitude={index["longitude"]}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,wind_speed_10m,wind_direction_10m,rain')
    weather=p.json()
    currWeather=weather["current"]
    #print(weather)

    print("\n")
    print(f"TimeZone: {weather["timezone"]}")
    time.sleep(0.25)
    print(f"Time: {currWeather["time"]}")
    time.sleep(0.25)
    print(f"Temperature: {currWeather["temperature_2m"]} °C")
    time.sleep(0.25)
    print(f"Relative Humidity: {currWeather["relative_humidity_2m"]} %")
    time.sleep(0.25)
    print(f"Apparent Temperature: {currWeather["apparent_temperature"]} °C")
    time.sleep(0.25)
    print(f"Is_Daytime: {currWeather["is_day"]}")
    time.sleep(0.25)
    print(f"Wind Speed: {currWeather["wind_speed_10m"]} km/h")
    time.sleep(0.25)
    print(f"Wind Direction: {currWeather["wind_direction_10m"]} °")
    time.sleep(0.25)
    print(f"Rain: {currWeather["rain"]} mm")
    time.sleep(1.5)
    print("\n Press any key to return")
    msvcrt.getch()
    mainScreen()

def gameCore():
    os.system("cls")
    cities = [
    # --- Top 20 Indian Cities ---
    {"city": "Mumbai", "state": "Maharashtra", "lat": 19.0760, "lon": 72.8777},
    {"city": "Delhi", "state": "Delhi (NCT)", "lat": 28.7041, "lon": 77.1025},
    {"city": "Bengaluru", "state": "Karnataka", "lat": 12.9716, "lon": 77.5946},
    {"city": "Hyderabad", "state": "Telangana", "lat": 17.3850, "lon": 78.4867},
    {"city": "Ahmedabad", "state": "Gujarat", "lat": 23.0225, "lon": 72.5714},
    {"city": "Chennai", "state": "Tamil Nadu", "lat": 13.0827, "lon": 80.2707},
    {"city": "Kolkata", "state": "West Bengal", "lat": 22.5726, "lon": 88.3639},
    {"city": "Surat", "state": "Gujarat", "lat": 21.1702, "lon": 72.8311},
    {"city": "Pune", "state": "Maharashtra", "lat": 18.5204, "lon": 73.8567},
    {"city": "Jaipur", "state": "Rajasthan", "lat": 26.9124, "lon": 75.7873},
    {"city": "Lucknow", "state": "Uttar Pradesh", "lat": 26.8467, "lon": 80.9462},
    {"city": "Kanpur", "state": "Uttar Pradesh", "lat": 26.4499, "lon": 80.3319},
    {"city": "Nagpur", "state": "Maharashtra", "lat": 21.1458, "lon": 79.0882},
    {"city": "Indore", "state": "Madhya Pradesh", "lat": 22.7196, "lon": 75.8577},
    {"city": "Patna", "state": "Bihar", "lat": 25.5941, "lon": 85.1376},
    {"city": "Bhopal", "state": "Madhya Pradesh", "lat": 23.2599, "lon": 77.4126},
    {"city": "Visakhapatnam", "state": "Andhra Pradesh", "lat": 17.6868, "lon": 83.2185},
    {"city": "Varanasi", "state": "Uttar Pradesh", "lat": 25.3176, "lon": 82.9739},
    {"city": "Ludhiana", "state": "Punjab", "lat": 30.9010, "lon": 75.8573},
    {"city": "Agra", "state": "Uttar Pradesh", "lat": 27.1767, "lon": 78.0081},

    # --- 30 Foreign Cities ---
    {"city": "New York", "state": "USA", "lat": 40.7128, "lon": -74.0060},
    {"city": "London", "state": "UK", "lat": 51.5074, "lon": -0.1278},
    {"city": "Paris", "state": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Tokyo", "state": "Japan", "lat": 35.6895, "lon": 139.6917},
    {"city": "Beijing", "state": "China", "lat": 39.9042, "lon": 116.4074},
    {"city": "Shanghai", "state": "China", "lat": 31.2304, "lon": 121.4737},
    {"city": "Moscow", "state": "Russia", "lat": 55.7558, "lon": 37.6173},
    {"city": "Dubai", "state": "UAE", "lat": 25.2048, "lon": 55.2708},
    {"city": "Singapore", "state": "Singapore", "lat": 1.3521, "lon": 103.8198},
    {"city": "Sydney", "state": "Australia", "lat": -33.8688, "lon": 151.2093},
    {"city": "Melbourne", "state": "Australia", "lat": -37.8136, "lon": 144.9631},
    {"city": "Los Angeles", "state": "USA", "lat": 34.0522, "lon": -118.2437},
    {"city": "San Francisco", "state": "USA", "lat": 37.7749, "lon": -122.4194},
    {"city": "Toronto", "state": "Canada", "lat": 43.6532, "lon": -79.3832},
    {"city": "Vancouver", "state": "Canada", "lat": 49.2827, "lon": -123.1207},
    {"city": "Berlin", "state": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Munich", "state": "Germany", "lat": 48.1351, "lon": 11.5820},
    {"city": "Rome", "state": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Madrid", "state": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Barcelona", "state": "Spain", "lat": 41.3851, "lon": 2.1734},
    {"city": "Istanbul", "state": "Turkey", "lat": 41.0082, "lon": 28.9784},
    {"city": "Seoul", "state": "South Korea", "lat": 37.5665, "lon": 126.9780},
    {"city": "Hong Kong", "state": "China", "lat": 22.3193, "lon": 114.1694},
    {"city": "Bangkok", "state": "Thailand", "lat": 13.7563, "lon": 100.5018},
    {"city": "Kuala Lumpur", "state": "Malaysia", "lat": 3.1390, "lon": 101.6869},
    {"city": "Cape Town", "state": "South Africa", "lat": -33.9249, "lon": 18.4241},
    {"city": "Johannesburg", "state": "South Africa", "lat": -26.2041, "lon": 28.0473},
    {"city": "Mexico City", "state": "Mexico", "lat": 19.4326, "lon": -99.1332},
    {"city": "Buenos Aires", "state": "Argentina", "lat": -34.6037, "lon": -58.3816},
    {"city": "São Paulo", "state": "Brazil", "lat": -23.5505, "lon": -46.6333}
    ]


    cont = 0
    score = 7

    os.system("cls")
    time.sleep(0.5)
    print("Loading",end="")
    time.sleep(0.35)
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
    time.sleep(0.5)


    while cont == 0 and score != 0:
        city = random.choice(cities)
        time.sleep(0.5)

        g=requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={city["lat"]}&longitude={city["lon"]}&current=weather_code,is_day').json()
        isDay = g["current"]["is_day"]
        weather = g["current"]["weather_code"]

        
        print("You wake up in a random place.")
        time.sleep(2)
        print("On the table in front of you,",end=" ")
        time.sleep(1.5)
        print("You see a table planner.")
        time.sleep(2)
        print(f"It reads city name {city["city"]}, {city["state"]}.")
        time.sleep(1)

        print("\nPress any key to continue.")
        msvcrt.getch()

        print("The whole room is dark.")
        time.sleep(1)
        print("\nYou reach out for your window")
        time.sleep(0.5)
        print("\nWhat do you think, is it day or night.\n")
        print("a) Day_time")
        print("b) Night_time\n")

        ch1=msvcrt.getch().decode()
        while(ch1 != 'a' and ch1 != 'b'):
            time.sleep(0.5)
            print("\nKindly Enter a valid response(a, b).\n")
            time.sleep(0.5)
            ch1=msvcrt.getch().decode()

        print("\nWhat do you think the weather would be out there?\n")
        time.sleep(0.75)
        print("a) Clear")
        time.sleep(0.5)
        print("b) Cloudy/Foggy")
        time.sleep(0.5)
        print("c) Rainy/Thunder Storm")
        time.sleep(0.65)

        ch2 = msvcrt.getch().decode()
        while(ch2 != 'a' and ch2 != 'b' and ch2 != 'c'):
            time.sleep(0.5)
            print("\nKindly Enter a valid response(a, b, c).")
            time.sleep(0.5)
            ch2=msvcrt.getch().decode()

        if ch1 == 'a' and isDay == 1:
            time.sleep(0.75)
            print("\nGreat Guess!")
            time.sleep(1)
            print("It was daytime.")

        elif ch1 == 'b' and isDay == 0:
            time.sleep(0.75)
            print("\nGreat Guess!")
            time.sleep(1)
            print("It was night-time.")

        else:
            time.sleep(0.75)
            print("\nWrong Guess.")
            score = score - 1
            time.sleep(0.85)
            if isDay == 1:
                print("It was daytime.")
            if isDay == 0:
                print("It was night-time.")
            
        time.sleep(2)
        print("\nYou see the weather out there.\n")
        time.sleep(2)

        if ch2 == 'a' and weather == 0 or weather == 1:
            print("Correct Guess!\n")
            time.sleep(0.85)
            print("The weather was clear and calm.\n")
            time.sleep(2)
        
        elif ch2 == 'b' and weather > 1 and weather < 50:
            print("Correct Guess!\n")
            time.sleep(0.85)
            print("The weather was cloudy and foggy.")
            time.sleep(1.5)
            print("Mysterious as if something is yet to arrive.\n")
            time.sleep(2)

        elif ch2 == 'c' and weather > 50:
            print("Correct Guess!\n")
            time.sleep(0.85)
            print("The weather was rainy and fierce.")
            time.sleep(1.5)
            print("As if it was a warning...\n")
            time.sleep(2)

        else:
            if weather == 0 or weather == 1:
                print("You were wrong\n")
                score = score - 1
                time.sleep(1)
                print("It was surpringly calm outside,",end=" ")
                time.sleep(0.5)
                print("Really calm.\n")
                time.sleep(1.5)

            elif weather > 1 and weather < 50:
                print("You are surprised.\n")
                score = score - 1
                time.sleep(1)
                print("The cloudy and foggy weather outside felt very different.")
                time.sleep(1)
                print("You felt a chill passing through your body.\n")
                time.sleep(2)

            elif weather > 50:
                print("To your surprise,",end=" ")
                score = score - 1
                time.sleep(0.5)
                print("The weather was ferocious.")
                time.sleep(1)
                print("You were feeling afraid.\n")
                time.sleep(2)

        print(f"Your Score: {score}, Dont let it go zero, it reduces everytime you do a wrong guess.")
        print("Press c if you want to continue, otherwise press any key to exit.")
        
        ch3 = msvcrt.getch().decode()
        if ch3 == 'c':
            cont = 0
        else:
            cont = 1

    os.system("cls")
    print("You suddenly wake up.")
    time.sleep(1.5)
    print("It was all a dream.")
    time.sleep(2)
    return

mainScreen()