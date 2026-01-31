import requests

# Example 2
api_url = "https://api.example.com/data?type=latest&limit=5"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print("Data received from url:", data)
else:
    print("Failed to receive data")

# Examples in Python
api_url = "https://api.example.com/weather"

parameters = {
    "city": "Bishkek",
    "apikey": "your_api_key"
}

response = requests.get(api_url, params=parameters)

if response.status_code == 200:
    data = response.json()
    print("Current weather data:")
    print(data)
else:
    print("Failed to retrieve data")
    print("Status code:", response.status_code)