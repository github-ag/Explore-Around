# Save the excel sheet as .csv file

import getpass      # For hiding password input
import csv      # For reading excel sheet
import smtplib, ssl     # For Security
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

passwordChoice = input("Do you want your password to be shown on screen Y/N ")

mailServer = input("Type mail server and press Enter :")
CSVFileName = input("Type csv file name and press Enter :")
sender_email = input("Type sender email and press Enter :")
if passwordChoice == 'Y' or passwordChoice == 'y':
    password = input("Type your password and press Enter :")     # Taking password input from user
elif passwordChoice == 'N' or passwordChoice == 'n':
    password = getpass.getpass(prompt="Type your password and press Enter :",stream=None)

message = MIMEMultipart("alternative")

message["Subject"] = input("Enter subject of Email and press Enter :")       # Enter subject here
message["From"] = sender_email                  # Enter Email id from which you want to send

# Create the plain-text and HTML version of your message
text1 = """
Hi """
text2 = """,
How are you?
Not seen you since long
Sachin
"""

html1 = """
<html>
  <body>
    <img src="https://i.postimg.cc/RCDr27GC/Hello.png">
    <p>Hi """
html2 = """,<br>
How are you?
<br>Not seen you since long
<br><br><b>Sachin</b>
  </body>
</html>"""

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp." + mailServer + ".com", 465, context=context) as server:
    server.login(sender_email, password)
    with open(CSVFileName) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, subs, avg, email, contact, pricing in reader:
            if len(email) > 0 and email.find("@") != -1:
                receiver_email = email

                # Building Message
                text = text1 + f"{name}" + text2
                html = html1 + f"{name}" + html2
                part1 = MIMEText(text, "plain")
                part2 = MIMEText(html, "html")

                message.attach(part1)
                message.attach(part2)
                server.sendmail(sender_email, receiver_email, message.as_string())
