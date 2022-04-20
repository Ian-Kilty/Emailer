# Usage python mailer.py <file> -> email, subject, var1, var2... <file> -> body text with variables defined with <>
# body.txt Ex. Hello {data[0]}, how are you doing this data[1]? -> must be one line
# {data[0]} is sent as the variable put in var1 in the arguments

# Make sure your email accout is authorized with https://myaccount.google.com/lesssecureapps

email = input("Email: ")
password = input("Password: ")
import sys
import smtplib
from email.message import EmailMessage
emails = []
subjects = []
bodys = []
template = ""
body = ""
f = open(str(sys.argv[1]), "r")
for x in f:
  x = x.split(",")
  data = x[2:len(x)]
  template = open(sys.argv[2], "r").read()
  body = template
  for i in range(len(data)):
    body = body[:body.find("{")] + data[i].strip() + body[body.find("}")+1:]
  emails.append(x[0])
  bodys.append(body)
  subjects.append(x[1].strip())
for i in range(len(emails)):
    msg = EmailMessage()
    subject = subjects[i]
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = emails[i]
    body1 = body
    msg.set_content(body1)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(msg)
        print("Sent to: " + emails[i] + " : " + subjects[i])