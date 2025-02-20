import requests
from pprint import pprint
import random

url = 'http://shortiki.com/export/api.php'

params =  {
    "format": "json",
    "amount": "100",
    "type":"top"
}

response = requests.get(url, params=params)
response.raise_for_status()
z = print(response.json()[random.randint(0,100)]['content'])

x = len(response.json())
print(x)
