import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime
from twilio.rest import Client



def convert(date_str):
  format = "%Y/%m/%d"  # Date will in from day/month/year
  return datetime.strftime(date_str, format).date() 

def web_requests():
  response = requests.request("GET", url, headers=headers, params=querystring)
  return web_requests() 
  pass

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
    
    
    
              
    

    airline = response.json()[0]["airline"]["name"]
  
    departure = response.json()[0]["departure"]["airport"]["name"]
  
    arrival = response.json()[0]["arrival"]["airport"]["name"]

    time = response.json()[0]["departure"]["scheduledTimeLocal"]
  
    image = response.json()[0]["aircraft"]["image"]["url"]
  #download image
    r = requests.get(image)
    with open('flight.jpg','wb') as f:
     f.write(r.content)
    
  
    print("This is a "+ airline +" flight.")
  
    print("Flying from  " + departure )
  
    print("To  " + arrival)
    print(time)

    return response.json()




x = flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"})

time = x[0]["departure"]["scheduledTimeLocal"]

def arrival_weather(city="london"):
  
  
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

  response = requests.request("GET", weather_api, headers=headers, params=querystring)

  print(response.json())



arrival_weather(x[0]["arrival"]["airport"]["name"])



def departure_weather(city="london"):
  
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

  response = requests.request("GET", weather_api, headers=headers, params=querystring)

  print(response.json())

departure_weather(x[0]["departure"]["airport"]["name"])



def message(time="00:00"):
  account_sid = 'ACdbc503bd8a56b87c39fef13cef888d41' 
  auth_token = 'de03ad3d82ddf4e015063ad8084cc95f' 
  client = Client(account_sid, auth_token) 
 
  message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your flight will be leaving at ' + time  ,      
                              to='whatsapp:+447469504601' 
                          ) 
 
  print(message.sid)

message(x[0]["departure"]["scheduledTimeLocal"])