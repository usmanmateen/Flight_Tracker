
from twilio.rest import Client
 

 
account_sid = 'ACdbc503bd8a56b87c39fef13cef888d41' 
auth_token = 'de03ad3d82ddf4e015063ad8084cc95f' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+447469504601' 
                          ) 
 
print(message.sid)