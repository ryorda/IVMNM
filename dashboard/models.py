from django.db import models

class Account(models.Model) :
	name 		= models.CharField(max_length=32)
	birthdate 	= models.DateField()
	
	def __str__(self) :
		return self.name