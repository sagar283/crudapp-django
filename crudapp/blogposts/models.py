from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date_posted = models.DateField()

	def __str__(self):
		return self.title