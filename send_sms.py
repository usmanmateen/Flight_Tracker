
from twilio.rest import Client
 

 



 
account_sid = 'ACd34af5eac16e272e32fa284bcbe73c37' 
auth_token = '72932a801079083300e1f203c2fdf910' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGc9184851d45f6b1e92c55477f0390342', 
                              body='hi',      
                              to='+447469504601' 
                          ) 
 
print(message.sid)