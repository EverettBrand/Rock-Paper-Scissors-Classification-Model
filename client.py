import requests
import sys

url = "http://localhost:5000/name"

r = requests.post(url)
print(r.text)

url = "http://localhost:5000/api"

path=sys.argv[1]

r = requests.post(url, json={'exp': path})

print('The image you’ve submitted is classified as a: ' + r.json())




