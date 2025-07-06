# https://myaccount.google.com/

import smtplib
from email.mime.text import MIMEText

my_email="..." # sender email
my_password="..." # your Gmail app password
receiver_email="..." # receiver email
# msg="Subject:Hello\n\nThis is the body of the email."
msg = MIMEText("Hello, this is your weather update!", "plain", "utf-8")
msg["Subject"] = "Daily Weather Update"
msg["From"] = "youremail@gmail.com"
msg["To"] = "friend@example.com"

connection=smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=my_email,password=my_password)
connection.sendmail(from_addr=my_email,to_addrs=receiver_email,msg=msg.as_string())
connection.close()
print("Email sent successfully!")