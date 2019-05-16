# Create your models here.
# filename: first_site/votings/models.py

from django.db import models

class MailID(models.Model):
	mail = models.CharField(max_length = 20)
	# question_text = models.CharField(max_length = 200)
	# pub_date = models.DateTimeField('Published date')

class Password(models.Model):
	mail = models.ForeignKey(MailID, on_delete = models.CASCADE)
	password = models.CharField(max_length = 50)
	# votes = models.IntegerField(default = 0)
