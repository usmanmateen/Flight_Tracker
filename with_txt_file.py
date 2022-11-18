import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os


load_dotenv('key.env')

def send_chat_log():


# Set up the email 
  bot_email = "flightbotdiscord@gmail.com"
  user_email = str(input('Whats is your email:'))

# Retreive password from key.env
  password = os.getenv('pswd')

   # Body of the email
  body = "Hi, a copy of your chat transcript is attached below."

  # MIME object to define email's parts
  message = MIMEMultipart()
  message['From'] = "Flight Bot" #Name of the bot on the email
  message['To'] = user_email
  message['Subject'] = "Discord chat log"

 # Attach body of the message
  message.attach(MIMEText(body, 'plain'))

  #identify file
  file_name = "conversation.txt"

  #code below is some what similar to The Intrigued Engineer in his youtube video.
  attachment= open(file_name, 'rb') #opens given file in binary.

  # encrypt in 64 form.
  attachment_package = MIMEBase('application', 'octet-stream')
  attachment_package.set_payload((attachment).read())
  encoders.encode_base64(attachment_package)
  attachment_package.add_header('Content-Disposition', "attachment; file_name= " + file_name)
  message.attach(attachment_package)

   
  text = message.as_string()

  # Connect with the server
  try:
      print("Connecting to server")
      gmail_server = smtplib.SMTP("smtp.gmail.com", 587)
      gmail_server.starttls()
      gmail_server.login(bot_email, password)
      print("Succesfully connected to server")
     


      # Send emails to "person" as list is iterated
      print("Sending email to:" + user_email +" ...")
      gmail_server.sendmail(bot_email, user_email, text)
      print("Email sent to: " + user_email)
      print()
  except:
      print("Something went wrong")
  #code above is some what similar to The Intrigued Engineer in his youtube video.
  # Close the port
  gmail_server.quit()


# Run the function
send_chat_log()
