
import requests
from datetime import date, datetime




flight = input("what is the flight number: ")
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
date1 = str(date(year, month, day))


url1 = "https://aerodatabox.p.rapidapi.com/flights/number/"
urlFinal = url1+flight+"/"+date1

querystring = {"withAircraftImage":"true","withLocation":"true"}

headers = {
	"X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request(
  
  "GET", urlFinal, headers=headers, params=querystring)



airline = response.json()[0]["airline"]["name"]

departure = response.json()[0]["departure"]["airport"]["name"]

arrival = response.json()[0]["arrival"]["airport"]["name"]

print("This is a "+airline+" flight.")

print("Flying from  " + departure )

print("To  " + arrival)


