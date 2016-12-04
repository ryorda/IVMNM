from django.db import models

class User(models.Model) :
	username = models.ForeignKey('auth.User')
	password = models.CharField(max_length=32)
	account = models.ForeignKey('dashboard.Account')
	
	def __str__(self) :
		return self.username
	