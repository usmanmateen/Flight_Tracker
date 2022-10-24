import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime

def convert(date_str):
  format = "%Y/%m/%d"  # Date will in from day/month/year
  return datetime.strftime(date_str, format).date() 

def web_requests():
  response = requests.request("GET", url, headers=headers, params=querystring)
  return web_requests()  

def flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"}):
    flight = input("what is the flight number: ")
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
  
    

    try:
      date1 = str(date(year, month, day))
              
    except:
      print("Date Error")
      return flight_data()
      
      
    api = "https://aerodatabox.p.rapidapi.com/flights/number/"
    url = api + flight +"/"+date1
      
  
    headers = {
      "X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
      }
  
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    
    return (response.json())
              
    
    return flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"})
  





def arrival_weather(city="london"):
  
  
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

  response = requests.request("GET", weather_api, headers=headers, params=querystring)

  print(response.json())


x = flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"})

arrival_weather(x[0]["arrival"]["airport"]["name"])


