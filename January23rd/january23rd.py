import json
import requests

#https://github.com/EricCharnesky/CIS1501-Fall2019/blob/8465629b2382cdeb72167ec5ebbbb7438234572e/November14th-IO/fileio.py

response = requests.get("https://api.noopschallenge.com/mazebot/random?minSize=10&maxSize=10")

if response.ok:
    response_body = json.loads(response.content)
    for row in response_body["map"]:
        print(row)
