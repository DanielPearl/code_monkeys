import json
import requests

parameters = {}
response = requests.get("https://api.population.io:80/1.0/population/{coutry}/today-and-tomorrow/", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
name = data["date"]["population"]
for item in items:
    print(item[8] + ": " + item[9])
