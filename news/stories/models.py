# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from urlparse import urlparse


class Story(models.Model):
	title = models.CharField(max_length=250, verbose_name=u'Заголовок')
	url = models.URLField()
	points = models.IntegerField(default=1, verbose_name=u'Очки')
	moderator = models.ForeignKey(User, related_name='moderated_stories', verbose_name=u'Модератор')
	voters = models.ManyToManyField(User, related_name='liked_stories')
	created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создан')
	updated = models.DateTimeField(auto_now=True, verbose_name=u'Обновлен')
	
	
	def domain(self):
		return urlparse(self.url).netloc

	domain.short_description = u'Домен'

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'story'
		verbose_name_plural = u'stories'