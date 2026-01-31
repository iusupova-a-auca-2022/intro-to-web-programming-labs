import requests
from flask import Flask, jsonify, request

# Example 1
api_url = "https://api.coingecko.com/api/v3/coins/markets"

parameters = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": "false"
}

response = requests.get(api_url, params=parameters)

if response.status_code == 200:
    content = response.json()

    for coin in content:
        print(f"{coin["name"]}: ${coin["current_price"]}")
else:
    print("Failed to retrieve data:", response.status_code)

# Example 2
app = Flask(__name__)

weather_data = {
    "London": {"temperature": 10, "condition": "Cloudy"},
    "New York": {"temperature": 19, "condition": "Sunny"},
    "Bishkek": {"temperature": 0, "condition": "Snowy"}
}

@app.route("/weather", methods=["GET"])

def get_weather():
    city = request.args.get("city")

    if city in weather_data:
        return jsonify({city: weather_data[city]})
    else:
        return jsonify({"Failed to find city"}), 404

if __name__ == "__main__":
    app.run(debug=True)