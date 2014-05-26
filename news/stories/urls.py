from django.conf.urls import patterns, include, url


urlpatterns = patterns('stories.views', 

    url(r'^$', 				'index', 		name='index'),
    url(r'^story/$', 		'story', 		name='create_story'),
    url(r'^vote/$', 		'vote', 		name='vote'), 
)