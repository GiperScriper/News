from django.conf.urls import patterns, include, url


urlpatterns = patterns('stories.views',   


    url(r'^$', 'index', name='home'),
    url(r'^story/$', 'story', name='create_story'),
    #url(r'^login/$', 'login', name='login'),
    
)

urlpatterns += patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', { 'template_name' : 'stories/login.html' }),
)
