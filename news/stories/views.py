# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from annoying.decorators import render_to
from django.utils.timezone import utc
from django.contrib.auth.decorators import login_required

from .models import Story
from .forms import StoryForm

from datetime import datetime


def index(request):
	stories = Story.objects.all().order_by('-created')

	if request.user.is_authenticated():
		liked_stories = request.user.liked_stories.filter(id__in = [ story.id for story in stories ])
	else:
		liked_stories = []

	return render(request, 'stories/index.html', locals())


@login_required
def story(request):
	if request.method == 'POST':
		form = StoryForm(request.POST)
		if form.is_valid():
			story = form.save(commit=False)
			story.moderator = request.user
			story.save()
			return HttpResponseRedirect('/')
	else:
		form = StoryForm()

	return render(request, 'stories/create.html', locals())


@login_required
def vote(request):
	story = get_object_or_404(Story, pk=request.POST.get('story'))	
	story.points += 1
	story.save()
	user = request.user
	user.liked_stories.add(story)
	user.save()
	return HttpResponse()