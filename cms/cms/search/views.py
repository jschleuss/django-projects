from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage

def search(request):
    query = request.GET['q']
    return render_to_response('search/search.html',
      { 'query': query,
        'results': transit.objects.filter( route_name__icontains=query) })
