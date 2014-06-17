from django.test import TestCase
import unittest

from stories.models import Story
from django.contrib.auth.models import User
from .serializers import StorySerializer
from rest_framework.renderers import JSONRenderer
from collections import OrderedDict

class StorySerializerTests(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.u = User(name="test", email="test@test.com")
		cls.u.save()

		cls.new_title = Story(moderator=cls.u, title="hello world")
		cls.new_title.save()