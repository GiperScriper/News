from django.conf.urls import patterns, url
import views

urlpatterns = patterns('api.views',
	
	url(r'^stories/$', 						views.StoriesList.as_view() ),
	url(r'^stories/(?P<pk>[0-9]+)$', 		views.StorySingle.as_view() ),
)