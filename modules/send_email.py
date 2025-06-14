import smtplib
from email.message import EmailMessage

def send_email(to_email,subject,content):
  msg=EmailMessage()
  msg.set_content(content)
  msg['Subject']=subject
  msg['From']="kardev321@gmail.com"
  msg['To']=to_email

  with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server.login("kardev321@gmail.com","app_password")
    server.send_message(msg)
    