#importing libraries
import requests
from datetime import date, datetime



#Allows me to get user input.
flight = input("what is the flight number: ")
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))



#Allows me to combine year, date and month in a sequence to later use.
date1 = str(date(year, month, day))

# Url is imcomplete and in the next stage it gets last extension
url1 = "https://aerodatabox.p.rapidapi.com/flights/number/"

#Concatinate url with flight info and date
urlFinal = url1+flight+"/"+date1

#string to get data froom the API
querystring = {"withAircraftImage":"true","withLocation":"true"}


#Headers contain my key to access flight data
headers = {
	"X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}


response = requests.request(
  # get response 
  "GET", urlFinal, headers=headers, params=querystring)


#following are the variables which exact respective data from JSON.

airline = response.json()[0]["airline"]["name"]qwe123

departure = response.json()[0]["departure"]["airport"]["name"]

arrival = response.json()[0]["arrival"]["airport"]["name"]


print("This is a "+airline+" flight.")

print("Flying from  " + departure )

print("To  " + arrival)


