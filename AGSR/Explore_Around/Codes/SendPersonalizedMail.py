#https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
#https://support.google.com/accounts/answer/6010255
#https://myaccount.google.com/lesssecureapps

import smtplib, ssl     # For Security
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMailFunction(name,mail,subject,query):
	mailServer = 'gmail'
	#sender_email = 'gotravel.agsr@gmail.com'
	sender_email = 'sachinroy290@gmail.com'
	password = ''
	receiver_email = 'sachinroy784@gmail.com'

	message = MIMEMultipart("alternative")

	message["Subject"] = 'Query from Explore Around form - ' + subject
	message["From"] = sender_email
	
	text = 'Name : ' + name + '\nMail : ' + mail + '\nQuery : ' + query
	htmlTemp1 = '<html> <body>'
	htmlTemp2 =		'<strong>Name : </strong> ' + name
	htmlTemp3 =		'<br><strong>Mail : </strong> ' + mail
	htmlTemp4 =		'<br><strong>Query : </strong> ' + query
	htmlTemp5 =	'</body> </html>'
	
	html = htmlTemp1 + htmlTemp2 + htmlTemp3 + htmlTemp4 + htmlTemp5
	
	# Create secure connection with server and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp." + mailServer + ".com", 465, context=context) as server:
		server.login(sender_email, password)

		# Building Message
		part1 = MIMEText(text, "plain")
		part2 = MIMEText(html, "html")

		message.attach(part1)
		message.attach(part2)
		currSend = server.sendmail(sender_email, receiver_email, message.as_string())
		if(len(currSend) == 0):
			return "Our team will contact you soon"
		return "Mail not sent"

