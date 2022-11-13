list_p='2022-11-10 04:38+05:00'
list = list(list_p)
print(''.join(list[10:16]))



def convert(date_str):
  format = "%Y/%m/%d"  # Date will in from day/month/year
  return datetime.strftime(date_str, format).date() 

def web_requests():
  response = requests.request("GET", url, headers=headers, params=querystring)
  return web_requests() 
  pass