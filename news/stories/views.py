# -*- coding: utf-8 -*-

from django.shortcuts import render
from annoying.decorators import render_to
from django.utils.timezone import utc

from .models import Story

from datetime import datetime


def score(story, gravity=1.8, timebase=120):
	points = story.points**0.8
	now = datetime.utcnow().replace(tzinfo=utc) # аналогично datetime.now()
	age = int((now - story.created).total_seconds()) / 60

	return points / (age*timebase)**gravity


def top_stories(top=180, consider=1000):
	latest_stories = Story.objects.all().order_by('-created')[:consider]
	ranked_stories = [ (score(story), story) for story in latest_stories ]
	return [ story for _, story in ranked_stories[:top] ]

@render_to('stories/index.html')
def index(request):
	stories = Story.objects.all().order_by('-created')
	now = datetime.utcnow().replace(tzinfo=utc)
	date_from_obj = stories[0].created

	age_in_minutes = int((now - date_from_obj).total_seconds()) / 60 
	return locals()