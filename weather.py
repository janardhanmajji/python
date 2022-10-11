import json
import requests

api_key = "db0ff65a75bb889bafe0a15fb526df36"
city = "Orlando"
url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=db0ff65a75bb889bafe0a15fb526df36"

request = requests.get(url)
json = request.json()
print(json)
