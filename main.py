import re
import complicate_rep as rep
import requests
from datetime import date, datetime


def input_chance(user_input, known_words, single_response=False, required_words=[])
 input_chance = 0
 has_required_words = True

#Calculate how many words are i the array from the message 
  for word in the user_input:
   if word in known_words:
      input_chance +=1
     
#Calculates % of known_words in user_input
     
  percentage = float(input_chance) / float(len(known_words))

  for word in known_words:
   if word not in user_input:
      has_required_words = False
      break
  if has_required_words or single_response
      return int(percentage*100)
  else:
    return 0


def check_all_messages(message):
  high_chance_list = {}

  def response(bot_response, list_of_words, single_response =False, required_words=[]):
    nonlocal hightest_prob_list
    highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Response_____________
  response('Hello!', ['hi', 'hello', 'wassup', 'hey'], single_response=True)
  response("I'am doing food what about you?", [ 'how', 'are', 'you', 'doing'], required_words= ['how'])

  response('Hello!', ['hi', 'hello', 'wassup', 'hey'], single_response=True)

















  
def fetch_rep(user_input):
 split_input = re.split(r'\s+|[!,.?-+_&'\]\s*, user_input.lower())
 response = check_all_messages(split_input)
 return rsponse





 
#Trying output
while true:
 print('ChatBot: ' + fetch_rep(input('You: ')))













































flight = input("what is the flight number: ")
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

date1 = str(date(year, month, day))

print(date1)

url1 = "https://aerodatabox.p.rapidapi.com/flights/number/"
urlFinal = url1+flight+"/"+date1

querystring = {"withAircraftImage":"true","withLocation":"true"}

headers = {
	"X-RapidAPI-Key": "7fd9c4ad4fmshd8f66ec397141d0p135583jsnc53fe7e95b0f",
	"X-RapidAPI-Host": "aerodatabox.p.rapidapi.com"
}

response = requests.request(
  
  "GET", urlFinal, headers=headers, params=querystring)

airline = response.json()[0]["airline"]["name"]

departure = response.json()[0]["departure"]["airport"]["name"]

arrival = response.json()[0]["arrival"]["airport"]["name"]

print("This is a "+airline+" flight.")

print("Flying from  " + departure )

print("To  " + arrival)

