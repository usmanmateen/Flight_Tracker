import requests

url = "https://aerodatabox.p.rapidapi.com/flights/number/LO15/2022-10-04"

querystring = {"withAircraftImage":"true","withLocation":"true"}

headers = {
	"X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())