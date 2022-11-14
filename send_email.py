import smtplib
import ssl

smtp_port = 587
smtp_server = "smtp.gmail.com"



message = MIMEMultipart()
message ["from"] = "Flight Bot"
message ["to"] = "tusmanmateen255@gmail.com"
message ["subject"] = "Transcript of your recent conversation"
message. attach (MIMEText ("Body"))

with smtplib.SMTP(host = "smtp.gmail.com", port= 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("flightbotdiscord@gmail.com","fnnxnxsqkefsxpbr")
    smtp.send_message()
    print("sent...")




fnnxnxsqkefsxpbr