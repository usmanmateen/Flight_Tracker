import requests
import urllib
import json
import urllib.request

url = "https://aerodatabox.p.rapidapi.com/flights/number/UX42/2022-10-11"

querystring = {"withAircraftImage":"true","withLocation":"true"}

headers = {
	"X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.json())




image = response.json()[0]["aircraft"]["image"]["url"]

r = requests.get(image)
with open('image.jpg','wb') as f:
  f.write(r.content)


  
print(image)


