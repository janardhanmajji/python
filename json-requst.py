import requests

dj = requests.get('http://api.open-notify.org/astros.json')
json = dj.json()
for person in json['people']:
    print(person['name'])