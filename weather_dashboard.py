# weather_dashboard.py

import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != 200:
        return f"Error: {data['message']}"
    return f"Weather in {city}: {data['main']['temp']}°C, {data['weather'][0]['description']}"

# Sample usage
print(get_weather("Istanbul"))
