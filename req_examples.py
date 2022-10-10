import requests as requests

base = 'https://api.translink.ca/rttiapi/v1/'
stops = 'stops/'
stop = '51658'

read = open('api_key.txt', 'r')
key = read.read()

params = {'apikey': key}
headers = {'application': 'json'}

response = requests.get(base + stops + stop, params=params)

with open('output.txt', 'a') as output:
    output.write(response.text + '\n')
