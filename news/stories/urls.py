from django.conf.urls import patterns, include, url


urlpatterns = patterns('stories.views',   


    url(r'^$', 'index', name='home'),
)
