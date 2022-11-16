import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime 
from twilio.rest import Client
from with_txt_file import send_chat_log
import time 


current_time = time.strftime("%H:%M:%S")
current_time_list = list(current_time)
time_check = ''.join(current_time_list[0:2])




#Loads key.env file for API keys
load_dotenv('key.env')

#Following function returns basic flight statistics with real-time location and aircraft image.
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
      
      #Standard API code for it to work
    api = "https://aerodatabox.p.rapidapi.com/flights/number/"
    url = api + flight +"/"+date1
      
  
    headers = {
      "X-RapidAPI-Key": os.getenv('flightAPI'),
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
      }
        #Standard API code for it to work
  
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    
    airline = response.json()[0]["airline"]["name"]
  
    departure = response.json()[0]["departure"]["airport"]["name"]
  
    arrival = response.json()[0]["arrival"]["airport"]["name"]

    time = response.json()[0]["departure"]["scheduledTimeLocal"]

    time_list= list(time)
    time_checker = ''.join(time_list[11:13])
    departure_time= ''.join(time_list[11:16])  


    
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

    if time_checker<time_check:
      print('Your flight was departed on '+departure_time)
    else:
      print('Your flight will depart on '+ departure_time)
    
  
    try:
      print(lat_lon)
    except:
      print("")

    return response.json()




x = flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"})

time = x[0]["departure"]["scheduledTimeLocal"]


def departure_time():
  time_list= list(time)
  time_checker = ''.join(time_list[11:13])
  departure_time= ''.join(time_list[11:16]) 
  
  if time_checker<time_check:
    d_time = str('Your flight was departed on '+departure_time)
    return d_time
  else:
    d_time = str('Your flight will depart on '+ departure_time)
    return d_time
departure_time()


# Following fuction returns an image of map with APIs taking latitude and longitude of the aircraft.
def map(lat,lon="0.00,0.00"):
  try:
    list_location = list(x[0]["location"].values())
  
    lat = str(list_location[4])
  
    lon = str(list_location[5])
    
  

    endpoint = 'https://maps.googleapis.com/maps/api/staticmap?center='
    map_size = '&zoom=7&size=400x400&markers=color:red%7Clabel:O%7C'
    marker = '&markers=size:mid%7Ccolor:0xFF0000%7C&key='
    #All API keys are stored in a seperate file called key.env and the following line is extracting that respective map key for this function to work
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




#Link example for MAP >>>>>>>>    https://maps.googleapis.com/maps/api/staticmap?center=52.47159, -1.76778&zoom=6&size=400x400&markers=color:blue%7Clabel:S%7C52.47159, -1.76778&markers=size:mid%7Ccolor:0xFFFF00%7Clabel:C%7CTok,AK%22&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E'



#Following function returns departure weather. It takes a city as parameter from the flight function and returns weather
def departure_weather(city="london"):

  #Standard API code for it to work
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": os.getenv('weatherAPI'),
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
  #Standard API code for it to work
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


#Following function returns arrival weather. It takes a city as parameter from the flight function and returns weather
def arrival_weather(city="london"):
  
  #Standard API code for it to work
  weather_api = "https://weatherapi-com.p.rapidapi.com/current.json"
  
  querystring = {"q":city}

  headers = {
	"X-RapidAPI-Key": os.getenv('weatherAPI'),
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
  #Standard API code for it to work
  
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


#Following function validates IATA airport code and returns false if code is wrong. If it is correct it passes these codes to be used in the next function.
def airport_code(airport = 'bhx',airport2 = 'lhr'):
  airport = str(input("3 digits airport code. Example: Bhx for Brirmingham > "))
  airport2 = str(input('3 digits airport code. Example:  LHR for London > '))
  
  if len(airport) == 3 and len(airport2) == 3:
    return airport, airport2
    
  else:
    return print(False)


#Following function takes IATA airport code afrom the previous function and returns estimated travel time between two given airports.
def airportDistance():
  
  list_arpt = list(airport_code())
  airport = list_arpt[0]
  airport2 = list_arpt[1]

  #Standard API code for it to work
  url = 'https://aerodatabox.p.rapidapi.com/airports/iata/'

  urlFinal = url + airport + "/distance-time/"+ airport2

  headers = {
	  "X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	  "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
  }
  #Standard API code for it to work
  response = requests.request("GET", urlFinal, headers=headers)

  approx = response.json()["approxFlightTime"]

  return print('Estimated flight time from ' +airport + ' to ' + airport2 +' is ' +approx)

airportDistance()


#Following function checks a UK number's format and returns the correct format of the number to be used in the next functio to send a message.
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
    
#Following function sends a message to the correct format number passed by previous function.
def message(time="00:00",flight_insight=x):

  
   #Standard API code for it to work
  account_sid = os.getenv('account_SID') 
  auth_token = os.getenv('Auth')  
  client = Client(account_sid, auth_token) 
  #Standard API code for it to work

  
  airline = str(x[0]["airline"]["name"])
  departure = str(x[0]["departure"]["airport"]["name"])
  arrival = str(x[0]["arrival"]["airport"]["name"])
  time = str(departure_time())

  
  #Standard API code for it to work
  message = client.messages.create( 
                                from_='+16208378159',  
                                body= "This is a "+ airline +" flight✈️." + " Flying from  " +   departure +"🛫." +" To  " + arrival + "🛩️." + '⏳ ' + time,      
                                to= number_check(),
                            ) 
   
  print(message.sid)
  #Standard API code for it to work

  
message(x[0]["departure"]["scheduledTimeLocal"],x[0])
 

  

  
  
