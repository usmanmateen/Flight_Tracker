import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "flightbotdiscord@gmail.com"
email_to = "usmanmateen255@gmail.com"

# Define the password (better to reference externally)
pswd = "fnnxnxsqkefsxpbr" # As shown in the video this password is now dead, left in as example only


# name the email subject
subject = "Discord chat log"



# Define the email function (dont call it email!)
def send_emails(email_to):

   # Make the body of the email
  body = f"""
  A copy of your transcript is attached below.
  """

  # make a MIME object to define parts of the email
  msg = MIMEMultipart()
  msg['From'] = email_from
  msg['To'] = email_to
  msg['Subject'] = subject

 # Attach the body of the message
  msg.attach(MIMEText(body, 'plain'))

  # Define the file to attach
  filename = "test_log.txt"

   # Open the file in python as a binary
  attachment= open(filename, 'rb')  # r for read and b for binary

  # Encode as base 64
  attachment_package = MIMEBase('application', 'octet-stream')
  attachment_package.set_payload((attachment).read())
  encoders.encode_base64(attachment_package)
  attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
  msg.attach(attachment_package)

   # Cast as string
  text = msg.as_string()

  # Connect with the server
  print("Connecting to server...")
  TIE_server = smtplib.SMTP(smtp_server, smtp_port)
  TIE_server.starttls()
  TIE_server.login(email_from, pswd)
  print("Succesfully connected to server")
  print()


  # Send emails to "person" as list is iterated
  print("Sending email to:" + email_to +" ...")
  TIE_server.sendmail(email_from, email_to, text)
  print("Email sent to: " + email_to)
  print()

  # Close the port
  TIE_server.quit()


# Run the function
send_emails(email_to)
