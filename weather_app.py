import requests

city = input("Enter city name: ")

while True:
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()
    if not geo_data.get("results"):
        print(f"'{city}' not found.")
        city = input("Please enter a valid city name: ")
        continue
    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    name = location["name"]
    country = location["country"]
    
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_data = requests.get(weather_url).json()
    
    current = weather_data["current_weather"]
    
    print(f"\nWeather in {name}, {country}:")
    print(f"Temperature: {current['temperature']}°C")
    print(f"Wind Speed: {current['windspeed']} km/h")
    print(f"Wind Direction: {current['winddirection']}°")
    again = input("\nDo you want to check another city? (Y/N): ")
    if again.lower() == "y":
        city = input("Enter city name: ")
    else:
        print("Goodbye!")
        break