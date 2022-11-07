import os
from dotenv import load_dotenv
import requests
from datetime import date, datetime


def flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"}):
  flight = input("what is the flight number: ")
  year = int(input('Enter a year: '))
  month = int(input('Enter a month: '))
  day = int(input('Enter a day: '))
  
  if flight.isalnum() == True and type(year)==int() and type(month) == int() and              type(date) == int():

    date = str(date(year, month, day))

    
    url = "https://aerodatabox.p.rapidapi.com/flights/number/"
    urlFinal = url + flight +"/"+date
    

    headers = {
    "X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	  "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
    }

    try:
        request = web_request(url,headers=headers,querystring)
        if type(request) is bool: # if False us returned 
            print("Error with Web Request")
            print(request)
            return "Not working"
        else:
            #convert_json_to_dict(web_request) if not in json form
            return request
            
    except:
        print("error")


    


def web_request(url,headers,querystring):
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
    except:
        print("Error in web_request")
        return False;

def convert_json_to_dict(json): # Extra if form need to be converted :) 
    try: 
        json = JSON.loads(json) # convert webrequest data into json dictionary if Json is given
        return json
    except:
        print("Unable to process JSON")
        return False;

  
querystring = {"withAircraftImage":"true","withLocation":"true"}


print(flight_data(querystring))
   