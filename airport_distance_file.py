import requests

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