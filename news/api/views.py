# -*- coding: utf-8 -*-

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .serializers import StorySerializer
from .permissions import IsOwnerOrReadOnly
from stories.models import Story


class StoriesList(generics.ListCreateAPIView):
	"""Get the list of all stories or create a new one"""	
	queryset = Story.objects.all()
	serializer_class = StorySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StorySingle(generics.RetrieveUpdateDestroyAPIView):
	"""Get, update or delete a story instance"""
	queryset = Story.objects.all()
	serializer_class = StorySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)