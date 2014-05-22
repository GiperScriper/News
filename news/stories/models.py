from django.db import models
from django.contrib.auth.models import User
from urlparse import urlparse


class Story(models.Model):
	title = models.CharField(max_length=250)
	url = models.URLField()
	points = models.IntegerField(default=0)
	moderator = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	@property
	def domain(self):
		return urlparse(self.url).netloc

	def __unicode__(self):
		return self.title

