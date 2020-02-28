# https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
# https://support.google.com/accounts/answer/6010255
# https://myaccount.google.com/lesssecureapps

import smtplib, ssl     # For Security
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid
import os
from django.conf import settings

def sendAutomatedReply(receiver_email, ref_num, result):
    mailServer = os.getenv('MAIL_SERVER')
    sender_email = os.getenv('MAIL_ID')
    password = os.getenv('MAIL_PASSWORD')

    # mailServer = 'gmail'
    # sender_email = 'gotravel.agsr@gmail.com'
    # password = 'AbhishekSachin'

    message = MIMEMultipart("alternative")

    message["Subject"] = 'Explore Around - Automated Reply - Reference No: ' + ref_num
    message["From"] = sender_email

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp." + mailServer + ".com", 465, context=context) as server:
        server.login(sender_email, password)

        # Building Message
        part = MIMEText(result, "plain")

        message.attach(part)
        currSend = server.sendmail(sender_email, receiver_email, message.as_string())

def sendMailFunction(name, mail_id, subject, query):
    mailServer = os.getenv('MAIL_SERVER')
    sender_email = os.getenv('MAIL_ID')
    password = os.getenv('MAIL_PASSWORD')
    receiver_email = os.getenv('MAIL_ID')

    # mailServer = 'gmail'
    # sender_email = 'gotravel.agsr@gmail.com'
    # password = 'AbhishekSachin'
    # receiver_email = 'gotravel.agsr@gmail.com'

    message = MIMEMultipart("alternative")

    subject_check = check_spam(subject, query)
    ref_num = str(uuid.uuid4().hex)
    message["Subject"] = subject_check + ' - ' + subject + ' - ' + ref_num
    message["From"] = sender_email

    text = 'Name : {}\nMail : {}\nQuery : {}'.format(name, mail_id, query)
    html = '''
            <html>
                <body>
                    <strong>Name : </strong>{}<br>
                    <strong>Mail : </strong>{}<br>
                    <strong>Query : </strong>{}
                </body>
            </html>
    '''.format(name, mail_id, query)

    result = '''
        Sorry your mail could not be sent.
        We regret the inconvenience caused.
        Try after sometime or you can contact us at 1234567890
    '''
    
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
            result = "Our team will contact you soon"
    try:
        sendAutomatedReply(mail_id, ref_num, result)
    except:
        pass
    return result


# ================== Checking Spam ====================
# Basic Libraries
import numpy as np 
import pandas as pd 

# Libraries for text cleaning
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer 

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Libraries for excessing the mail
import imaplib
import email

# Generating the training data
Mails_File = os.path.join(settings.BASE_DIR, 'Codes', 'Mails.txt')
with open(Mails_File,'r', encoding = 'utf-8') as file:
    data = file.readlines()

X = []
Y = []
for mail in data:
    mail_parts = mail.split('\t')
    label = mail_parts[0]
    message = ' '.join(mail_parts[1:])
    X.append(message)
    Y.append(label)

# Creating objects for data cleaning.
tokenizer = RegexpTokenizer(r'\w+')
sw = set(stopwords.words('english'))
ss = SnowballStemmer("english")

#Cleaning the text

def clean_mail(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace("\n","")
    word_list = tokenizer.tokenize(sentence)
    word_list = [w for w in word_list if w not in sw]
    final_list = [ss.stem(w) for w in word_list]
    new_sentence = ' '.join(final_list)

    return new_sentence


X_clean = [clean_mail(i) for i in X]

# Vectorization
cv = CountVectorizer(ngram_range=(1,2))
x_vec = cv.fit_transform(X_clean).toarray()

# Training the model
mnb = MultinomialNB()
mnb.fit(x_vec,Y)

def check_spam(subject_of_the_message, message):
    message = clean_mail(message)
    message = [message]
    message_vec = cv.transform(message)
    result = mnb.predict(message_vec)
    result = result[0]

    subjects = ['Query','Contact','Booking','Bug','Others']
    if result == 'ham':
        if subject_of_the_message in subjects[:-1]:
            return subject_of_the_message
        else:
            return 'Others'
    return 'spam'

