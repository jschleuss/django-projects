from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from transit.models import Route

def route_index(request):
	routes = Route.objects.all()
	return render_to_response('transit/route_index.html', {'routes':routes})
	
	# form pass routeID, use view to filter results based
	# view accepts form input and filters route results at submit
	
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RouteForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })