import os, requests, json

city = input("Enter city: ")

API_KEY = os.getenv('api_key')
API_URL = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY

response = requests.get(API_URL)

weather_data = response.json()

cityName = weather_data['name']
temp = weather_data['main'].get('temp') - 273.15
hum = weather_data['main'].get('humidity')

print("Temperature: ", temp)
print("Humidity: ", hum)