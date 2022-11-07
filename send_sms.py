import requests
r = requests.get('''https://maps.googleapis.com/maps/api/staticmap?center=50.4079718,-1.5051267&zoom=6&size=400x400&markers=color:blue%7Clabel:S%7C50.4079718,-1.5051267&markers=size:mid%7Ccolor:0xFFFF00%7Clabel:C%7CTok,AK"&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E''')
with open('map.jpg','wb') as f:
  f.write(r.content)




'https://maps.googleapis.com/maps/api/staticmap?center=52.56221, -1.86874&zoom=6&size=400x400&markers=color:blue%7Clabel:S%7C52.56221, -1.86874&markers=size:mid%7Ccolor:0xFFFF00%7Clabel:C%7CTok,AK"&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E'



&markers=icon:https://tinyurl.com/5953r55x


'https://maps.googleapis.com/maps/api/staticmap?center=50.4079718,-1.5051267&zoom=6&size=400x400&style=visibility:on&style=feature:water%7Celement:geometry%7Cvisibility:on&style=feature:landscape%7Celement:geometry%7Cvisibility:on&markers=anchor:topleft%7Cicon:https://tinyurl.com/5953r55x%7C50.4079718,-1.5051267&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E'




def map():
  endpoint =' https://maps.googleapis.com/maps/api/staticmap?center='
  middle = '&zoom=8&size=400x400&markers=color:red%7Clabel:S%7C'
  ,%20-9.08777 38.87158,%20-9.08777&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E
  latnlong= '38.87158'+',%20'+'-9.08777'
  
  api = endpoint+latnlong+middle+latnlong+'&key=AIzaSyBJM6palbsErzflk8nXqV4wWQdH_Zdg5_E'