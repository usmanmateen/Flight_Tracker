def flight_data(querystring = {"withAircraftImage":"true","withLocation":"true"}):
    flight = input("what is the flight number: ")
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
  
    date_str = f'{year}-{month}-{day}'

    if flight.isalnum():
          try:
              date = convert(date_str)
              
          except:
              print("Date Error")
              return flight_data()
      
          print("Date Erro")
          return flight_data() 
      
    url = "https://aerodatabox.p.rapidapi.com/flights/number/"
    urlFinal = url + flight +"/"+date
      
  
    headers = {
      "X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
        "X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
      }
  
    response = web_request(url,headers,querystring)
          
    print (response)
              
    
    return flight_data()
  
flight_data()