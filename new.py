import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime
from twilio.rest import Client



load_dotenv('key.env')
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
      "X-RapidAPI-Key": os.getenv('flightAPI'),
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
      }
  
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    
    airline = response.json()[0]["airline"]["name"]
  
    departure = response.json()[0]["departure"]["airport"]["name"]
  
    arrival = response.json()[0]["arrival"]["airport"]["name"]

    time = response.json()[0]["departure"]["scheduledTimeLocal"]


    image = response.json()[0]["aircraft"]["image"]["url"]

    try:
    
      real_time_geo = response.json()[0]["location"]
  
      list_location = list(real_time_geo.values())
  
      lat = list_location[4]
  
      lon = list_location[5]
    
      lat_lon = [lat,lon]
    except:
      print("Real time location for this flight is not available")

    
  #download image
    r = requests.get(image)
    with open('flight.jpg','wb') as f:
     f.write(r.content)
    
  
    print("This is a "+ airline +" flight.")
  
    print("Flying from  " + departure )
  
    print("To  " + arrival)
  
    print(time)
    try:
      print(lat_lon)
    except:
      print("")

    return response.json()




x = flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"})

time = x[0]["departure"]["scheduledTimeLocal"]



def departure_weather(city="london"):
  
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": os.getenv('weatherAPI'),
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

  response = requests.request("GET", weather_api, headers=headers, params=querystring)

  weather_C= response.json()["current"]["temp_c"]

  sky_state = response.json()["current"]["condition"]["text"]
  try:
    visibility = response.json()["current"]["condition"]["vis_miles"]
  except:
    print("")

  print("Current temperature in " + city +" is " +str(round(weather_C))+"°C")
  print("Sky is "+sky_state)
  try:
    print(visibility)
  except:
    print("")

departure_weather(x[0]["departure"]["airport"]["name"])



def arrival_weather(city="london"):
  
  
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": os.getenv('weatherAPI'),
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

  response = requests.request("GET", weather_api, headers=headers, params=querystring)

  weather_C= response.json()["current"]["temp_c"]

  sky_state = response.json()["current"]["condition"]["text"]
  try:
    visibility = response.json()["current"]["condition"]["vis_miles"]
  except:
    print("")

  print("Current temperature in " + city +" is " +str(round(weather_C))+"°C")
  print("Sky is "+sky_state)
  try:
    print(visibility)
  except:
    print("")
  
  return response.json()

  

arrival_weather(x[0]["arrival"]["airport"]["name"])



def number_check(number='+447196325410'):
  number = str(input("number?"))
  if number.startswith('+') == True:
    return number
  elif number.startswith('07') == True:
    list_num = list(number)
    num = ''.join(list_num[1:11])
    number = str("+44"+num)
    return number
  else:
    list_num = list(number)
    num = ''.join(list_num[2:14])
    number = str("+"+num)
    return number
    

def message(time="00:00",flight_insight=x):
   
  account_sid = os.getenv('account_SID') 
  auth_token = os.getenv('Auth')  
  client = Client(account_sid, auth_token) 
  
  airline = str(x[0]["airline"]["name"])
  departure = str(x[0]["departure"]["airport"]["name"])
  arrival = str(x[0]["arrival"]["airport"]["name"])
  time = str(x[0]["departure"]["scheduledTimeLocal"])
  
  message = client.messages.create( 
                                from_='+16208378159',  
                                body= "This is a "+ airline +" flight✈️." + " Flying from  " +   departure +"🛫." +" To  " + arrival + "🛩️." + " ⏳Departue time is " + time,      
                                to= number_check(),
                            ) 
   
  print(message.sid)

message(x[0]["departure"]["scheduledTimeLocal"],x[0])
