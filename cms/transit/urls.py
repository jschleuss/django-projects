from django.conf.urls import patterns
from transit.views import route_index

urlpatterns = patterns('',
	(r'^$', route_index),
)