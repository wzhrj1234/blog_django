from django.db import models

# Create your models here.

# The model of blog article
class BlogsPost(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField('date published')
