from django.conf.urls import patterns
from apps.transit.views import route_index
from django.views.decorators.cache import cache_page

urlpatterns = patterns('',
	(r'^$', cache_page(route_index)),
)