# Basic Libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

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
with open("Sample Mails.txt",'r')as file:
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

def check_spam(message):
    message = clean_mail(message)
    message = [message]
    message_vec = cv.transform(message)
    result = mnb.predict(message_vec)
    result = result[0]
    return result


# Getting the message,subject and senders info.

def get_message(idx):
    user = "gotravel.agsr@gmail.com"
    password = "AbhishekSachin"
    imap_url = "imap.googlemail.com"

    con = imaplib.IMAP4_SSL(imap_url)


    login = con.login(user,password)

    result,section_data = con.select('INBOX')
    number_of_mails = section_data[0].decode('utf-8')

    number_of_mails = int(number_of_mails)
    curr_mail = number_of_mails-idx
    curr_mail = str(curr_mail)
        
    # Getting last ith message
    result,data = con.fetch(curr_mail,'(RFC822)') #section_data[0] = no. of mails so we would get the last mail.        raw = email.message_from_bytes(data[0][1])
    raw = email.message_from_bytes(data[0][1])
    
    subject_of_the_message = raw['subject']
    senders_info = raw['from']
    senders_info = senders_info.split('<')
    senders_info = senders_info[1][:-1]
        
    message = raw.get_payload(0).get_payload(None,True)
    message = message.decode("utf-8")
    
    return subject_of_the_message,senders_info,message

def make_subjects_dictionary(subjects,no_of_messages_wanted):
    subjects_dictionary = {}
    for subject in subjects:
        subjects_dictionary[subject] = []
    
    for i in range(no_of_messages_wanted):
        subject_of_the_message,senders_info,message = get_message(i)
        
        if(check_spam(message)=='ham'):
            if subject_of_the_message in subjects[:-1]:
                subjects_dictionary[subject_of_the_message].append(senders_info)
            else:
                subjects_dictionary['Others'].append(senders_info)
    
    return subjects_dictionary
        
     
        
def printing_subjects_dictionary(dict):
    for key,value in dict.items():
        print(key,value)
    
subjects = ['Query','Contact','Booking','Bug','Others']
no_of_messages_wanted = 10
dict = make_subjects_dictionary(subjects,no_of_messages_wanted)
printing_subjects_dictionary(dict)
