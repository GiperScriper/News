# -*- coding: utf-8 -*-

from django.forms import widgets
from rest_framework import serializers
from stories.models import Story


class StorySerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Story
		fields = ('id', 'moderator', 'title', 'url', 'created')