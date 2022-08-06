import requests
import sys

url = "http://localhost:5000/name"

#returns and prints the server's information
r = requests.post(url)
print(r.text)

#server's url
url = "http://localhost:5000/api"

#takes filepath argument from command line when running client
path=sys.argv[1]

#sends server the image's path name and returns the identified image's classification
r = requests.post(url, json={'exp': path})

#prints jsonified classification
print('The image you’ve submitted is classified as a: ' + r.json())




