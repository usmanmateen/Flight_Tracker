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


def map(lat,lon="0.00,0.00"):
  try:
    list_location = list(x[0]["location"].values())
  
    lat = str(list_location[4])
  
    lon = str(list_location[5])
    
  

    endpoint = 'https://maps.googleapis.com/maps/api/staticmap?center='
    map_size = '&zoom=7&size=400x400&markers=color:red%7Clabel:O%7C'
    marker = '&markers=size:mid%7Ccolor:0xFF0000%7C&key='
    API =  os.getenv('maps')
    image_url = endpoint + lat+','+lon + map_size + lat+','+lon + marker + API

    r = requests.get(image_url)
    with open('flight_map.jpg','wb') as f:
      f.write(r.content)
    
  except:
    print('')
try:
  map(x[0]["location"])
except:
  print('')




#https://maps.googleapis.com/maps/api/staticmap?center=52.47159, -1.76778&zoom=6&size=400x400&markers=color:blue%7Clabel:S%7C52.47159, -1.76778&markers=size:mid%7Ccolor:0xFFFF00%7Clabel:C%7CTok,AK%22&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E'


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
 

  
def airport_code(airport = 'bhx',airport2 = 'lhr'):
  airport = str(input("3 digits airport code. Example: Bhx for Brirmingham > "))
  airport2 = str(input('3 digits airport code. Example:  LHR for London > '))
  
  if len(airport) == 3 and len(airport2) == 3:
    return airport, airport2
    
  else:
    return print(False)



def airportDistance():
  
  list_arpt = list(airport_code())
  airport = list_arpt[0]
  airport2 = list_arpt[1]

  
  url = 'https://aerodatabox.p.rapidapi.com/airports/iata/'

  urlFinal = url + airport + "/distance-time/"+ airport2

  headers = {
	  "X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	  "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
  }

  response = requests.request("GET", urlFinal, headers=headers)

  approx = response.json()["approxFlightTime"]

  return print('Estimated flight time from ' +airport + ' to ' + airport2 +' is ' +approx)

airportDistance()
  
  
