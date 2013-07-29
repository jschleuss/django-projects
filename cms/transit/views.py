from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from transit.models import Route

def route_index(request):
    routes = Route.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        selection = Route.objects.filter(route_name__exact=q)
        return render_to_response('transit/route_index.html', {'routes':routes, 'selection':selection, 'query':q})
    else:
        return render_to_response('transit/route_index.html', {'routes':routes})

