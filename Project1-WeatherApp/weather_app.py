import requests

try:
    city = input("Enter city name: ")

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url, timeout=10)

    data = response.json()

    temp = data["current_condition"][0]["temp_C"]
    weather = data["current_condition"][0]["weatherDesc"][0]["value"]
    humidity = data["current_condition"][0]["humidity"]

    print("\nWeather Details")
    print("Temperature:", temp, "°C")
    print("Weather:", weather)
    print("Humidity:", humidity, "%")

except Exception as e:
    print("Error:", e)