import requests

params = {
  'access_key': 'ce538ffdcd411e870fa8ba6d1e1d85f9'
}

api_result = requests.get('https://api.aviationstack.com/v1/flights/', params)

api_response = api_result.json()


print(api_response)