import smtplib
from email.message import EmailMessage
emails = []
subjects = []
bodys = []
f = open("emails.txt", "r")
for x in f:
  emails.append(x.split(",")[0])
  bodys.append(x.split(",")[1])
  subjects.append(x.split(",")[2].strip())
for i in range(len(emails)):
    msg = EmailMessage()
    subject = subjects[i] + " craigslist"
    msg['Subject'] = subject
    msg['From'] = 'iankilty98@gmail.com'
    msg['To'] = emails[i]
    body = "Hey my name is Ian and I saw your ad on craigslist for the " + bodys[i] + " and I was wondering if it is still available and if so if I can come pick it up? \n\nThank you!"
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('iankilty98@gmail.com', 'Office365Yahoo')
        smtp.send_message(msg)
        print("Sent to: " + emails[i] + " : " + subjects[i])