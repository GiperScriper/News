from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', 	include(admin.site.urls)),

    url(r'^', 			include('stories.urls')),
    url(r'^api/v1/', 	include('api.urls')),
    
    url(r'^login/$', 	'django.contrib.auth.views.login', 		{ 'template_name' : 'stories/login.html' }, 	name='login'),
    url(r'^logout/$', 	'django.contrib.auth.views.logout', 	{ 'next_page' : '/' }, 							name='logout'),
)
