from django.conf.urls import patterns, include, url


urlpatterns = patterns('stories.views',   


    url(r'^$', 'index', name='home'),
    url(r'^story/$', 'story', name='create_story'),
)
