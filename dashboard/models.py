from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Meal(models.Model) :
	name	= models.CharField(max_length=1024)
	calorie	= models.FloatField()
	imgurl  = models.URLField()
	
	def __str__(self) :
		return self.name

class History(models.Model) :
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
	meal 	= models.ForeignKey(Meal, on_delete=models.CASCADE, default=None, blank=True, null=True)
	time	= models.DateTimeField(default=now)
	
	def __str__(self) :
		return str(self.user) + " [" + str(self.meal) + "] @ " + str(self.time) 