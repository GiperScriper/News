# -*- coding: utf-8 -*-

from django.forms import widgets
from rest_framework import serializers
from stories.model import Story


class StorySerializer(serializers.Serializer):
	pk = serializers.Field()
	user = serializers.RelatedField(many=False)
	title = serializers.CharField(max_length=250)
	url = serializers.CharField()
	created = serializers.DateTimeField()