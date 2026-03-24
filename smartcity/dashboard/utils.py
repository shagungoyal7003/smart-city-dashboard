import requests

def get_weather():
    api_key = "dd40ad36972edf2b8f24cd1b610ff92b"   # put your key here
    city = "Delhi"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    # Debug print (optional)
    print(data)

    if response.status_code != 200:
        return None

    return {
        "city": city,
        "temp": data['main']['temp'],
        "humidity": data['main']['humidity']
    }