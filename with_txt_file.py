import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os


load_dotenv('key.env')
# Setup port number and server name

port = 587                 # Standard secure SMTP port
server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
bot_email = "flightbotdiscord@gmail.com"
user_email = str(input('Whats is your email:'))

# Define the password (better to reference externally)
password = os.getenv('pswd') # As shown in the video this password is now dead, left in as example only


# name the email subject
subject = "Discord chat log"



# Define the email function (dont call it email!)
def send_chat_log(user_email):

   # Make the body of the email
  body = f"""
  Hi, a copy of your chat transcript is attached below.
  """

  # make a MIME object to define parts of the email
  message = MIMEMultipart()
  message['From'] = "Flight Bot"
  message['To'] = user_email
  message['Subject'] = subject

 # Attach the body of the message
  message.attach(MIMEText(body, 'plain'))

  # Define the file to attach
  filename = "test_log.txt"

   # Open the file in python as a binary
  attachment= open(filename, 'rb')  # r for read and b for binary

  # Encode as base 64
  attachment_package = MIMEBase('application', 'octet-stream')
  attachment_package.set_payload((attachment).read())
  encoders.encode_base64(attachment_package)
  attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
  message.attach(attachment_package)

   # Cast as string
  text = message.as_string()

  # Connect with the server
  try:
      print("Connecting to server...")
      gmail_server = smtplib.SMTP(server, port)
      gmail_server.starttls()
      gmail_server.login(bot_email, password)
      print("Succesfully connected to server")
      print()


      # Send emails to "person" as list is iterated
      print("Sending email to:" + user_email +" ...")
      gmail_server.sendmail(bot_email, user_email, text)
      print("Email sent to: " + user_email)
      print()
  except:
      print("Something went wrong")

  # Close the port
  gmail_server.quit()


# Run the function
send_chat_log(user_email)
