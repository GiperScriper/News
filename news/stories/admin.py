# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Story


class StoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'domain', 'moderator', 'created', 'updated')
	list_filter = ('created', 'updated')
	search_fields = ('title', 'moderator__username')

	fieldsets = [
		(u'Новость', {
			'fields': ('title', 'url', 'points')
			}),

		(u'Модератор', {			
			'fields': ('moderator',)
			}),

		(u'История изменений', {
			'classes': ('collapse',),
			'fields': ('created', 'updated')
			}),		
	]

	#fields = ('title', 'url', 'points', 'moderator', 'created', 'updated')
	readonly_fields = ('created', 'updated')
	
admin.site.register(Story, StoryAdmin)