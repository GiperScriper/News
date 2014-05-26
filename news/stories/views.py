# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from annoying.decorators import render_to
from django.utils.timezone import utc

from .models import Story
from .forms import StoryForm

from datetime import datetime


def score(story, gravity=1.8, timebase=120):
	points = story.points**0.8
	now = datetime.utcnow().replace(tzinfo=utc)
	age = int((now - story.created).total_seconds()) / 60

	return points / (age*timebase)**gravity


def top_stories(top=180, consider=1000):
	latest_stories = Story.objects.all().order_by('-created')[:consider]
	ranked_stories = [ (score(story), story) for story in latest_stories ]
	return [ story for _, story in ranked_stories[:top] ]


@render_to('stories/index.html')
def index(request):
	stories = Story.objects.all().order_by('-created')
	
	return locals()


@render_to('stories/create.html')
def story(request):
	if request.method == 'POST':
		form = StoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(request, 'home')
	else:
		form = StoryForm()

	return locals()