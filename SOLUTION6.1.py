import requests

# user se city input lena
city = input("Enter city name: ")

# apni API key
api_key = "35eb88263ffcff413279efc279d3e209"

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"35eb88263ffcff413279efc279d3e209"}&units=metric"

# request bhejna
response = requests.get(url)

# JSON data lena
data = response.json()

# check karna city valid hai ya nahi
if response.status_code == 200:

    print("\n====== Weather Details ======\n")

    print("City:", data["name"])
    print("Country:", data["sys"]["country"])

    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")

    print("Minimum Temp:", data["main"]["temp_min"], "°C")
    print("Maximum Temp:", data["main"]["temp_max"], "°C")

    print("Humidity:", data["main"]["humidity"], "%")
    print("Pressure:", data["main"]["pressure"], "hPa")

    print("Weather Condition:", data["weather"][0]["main"])
    print("Description:", data["weather"][0]["description"])

    print("Wind Speed:", data["wind"]["speed"], "m/s")

    print("Visibility:", data["visibility"], "meters")

else:
    print("\nError:", data["message"])