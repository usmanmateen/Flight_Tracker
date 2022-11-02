import requests 

# -1 or False denotes an Error. Can be changed. 


def get_weather(querystring ={"lat":"0","lon":"0"} ):
    if querystring.get("lat") == "0" and querystring.get("lat") == "0":
        # checks if      there are default values are present 
        print("Not Arguments given returing -1")
        return False; 

    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/minutely"
    
    headers = {
        "X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    try:
        request = web_request(url,headers,querystring)
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
        return (response.text)
    except:
        print("Error in web_request")
        return False


def convert_json_to_dict(json): # Extra if form need to be converted :) 
    try: 
        json = JSON.loads(json) # convert webrequest data into json dictionary if Json is given
        return json
    except:
        print("Unable to process JSON")
        return False;
    

querystring = {"lat":"35.5","lon":"-78.5"}

print(get_weather(querystring)) # with args




date = convert(date_str)
            if not(datetime.now().date() >= date):
                print("Date is the past")
                return flight_data();



def re_get():
  image = response.json()[0]["aircraft"]["image"]["url"]
    r = requests.get(image)
    with open('flight.jpg','wb') as f:
     f.write(r.content)
pass




arrival_weather(x[0]["arrival"]["airport"]["name"])
print(departure_weather(x[0]["departure"]["airport"]["name"]))
