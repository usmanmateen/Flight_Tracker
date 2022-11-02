#importing libraries

import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime
from twilio.rest import Client 

  
try:
  load_dotenv('key.env')

  #Allows me to get user input.
  flight = input("what is the flight number: ")
  try:
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
  except:
    print("Date needs to be an integer")

    
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
  	"X-RapidAPI-Key": os.getenv('flightAPI'),
  	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
  }
  
  
  response = requests.request(
    # get response 
    "GET", urlFinal, headers=headers, params=querystring)
  
  #following are the variables which exact respective data from JSON.
  try:

    airline = response.json()[0]["airline"]["name"]
  
    departure = response.json()[0]["departure"]["airport"]["name"]
  
    arrival = response.json()[0]["arrival"]["airport"]["name"]
  
    image = response.json()[0]["aircraft"]["image"]["url"]
  #download image
    r = requests.get(image)
    with open('flight.jpg','wb') as f:
     f.write(r.content)
    
  
    print("This is a "+ airline +" flight.")
  
    print("Flying from  " + departure )
  
    print("To  " + arrival)
  except:
    print("Something went wrong")


except: 
  print("Something else went wrong")



  
account_sid = 'ACd34af5eac16e272e32fa284bcbe73c37'
auth_token = '72932a801079083300e1f203c2fdf910'
client = Client(account_sid, auth_token) 
     
message = client.messages.create( 
          from_='whatsapp:+14155238886',  
          body = "what is the flight number: " ,  
          to ='whatsapp:+447469504601' 
                              ) 
     
print(message.sid)