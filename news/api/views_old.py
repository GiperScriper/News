# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StorySerializer
from stories.models import Story


@api_view(['GET','POST'])
def stories_list(request):
	"""Get the list of all stories or create a new one"""
	

	if request.method == 'GET':
		stories = Story.objects.all()
		serializer = StorySerializer(stories, many=True)
		return Response(serializer.data)
	
	elif request.method == 'POST':
		serializer = StorySerializer(data=request.DATA)
	
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	
	return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def single_story(request, id):
	"""Get, update or delete a status_report instance"""

	try:
		story = Story.objects.get(id=id)
	
	except Story.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = StorySerializer(story)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = StorySerializer(story, data=request.DATA)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		story.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)