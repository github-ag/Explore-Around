import nltk
import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import imaplib,email

nltk.download_shell()
def get_message(mess):
    data = (mess.split('\t'))[1]
    return data
def get_type(mess):
    type = (mess.split('\t'))[0]
    return type
def text_process(mess):
    nopunc = [c for c in mess if c not in string.punctuation]
    nopunc = ''.join(nopunc)
    clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean_mess
def msgTonum(mess):
    mess = [mess]
    message_bow = bow_transformer.transform(mess)
    message_tfidf = tfidf_transformer.transform(message_bow)
    return message_tfidf

messages = [line.rstrip() for line in open('Mails.txt')]
df = pd.DataFrame()
df['messages']=messages
number_of_test_mails = len(df['messages'])
df['type'] = df['messages'].head(number_of_test_mails).apply(get_type)
df['messages']=df['messages'].head(number_of_test_mails).apply(get_message)
df['length']=df['messages'].head(number_of_test_mails).apply(len)

bow_transformer = CountVectorizer(analyzer=text_process).fit(df['messages'])
messages_bow = bow_transformer.transform(df['messages'])
tfidf_transformer = TfidfTransformer().fit(messages_bow)
messages_tfidf = tfidf_transformer.transform(messages_bow)
X_train = messages_tfidf
y_train = df['type']
model = MultinomialNB()
model.fit(X_train,y_train)

user = 'gotravel.agsr@gmail.com'
password = 'travel14&08'
imap_url = 'imap.googlemail.com'
con = imaplib.IMAP4_SSL(imap_url)
con.login(user,password)
con.select('INBOX')

#first testing on the single mail
result,data = con.fetch(b'5','(RFC822')
raw = email.message_from_bytes(data[0][1])
message = (raw.get_payload(0).get_payload(None,True))
message = message.decode('utf-8')

X_test = msgTonum(message)
prediction = spam_detect_model.predict(X_test)
print(prediction)
