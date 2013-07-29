from django.db import models
from django import forms

CHANGE_CHOICES = (
	('0', 'deleted'),
	('1', 'reduced'),
	('2', 'unchanged'),
)

class Route(models.Model):
	route_name = models.CharField(max_length=30)
	route_number = models.CharField(max_length=255)
	description = models.TextField()
	change = models.CharField(max_length=1,choices=CHANGE_CHOICES,blank=True)
	change_desc = models.TextField(blank=True)

	map_link = models.URLField(max_length=255,blank=True)
	schedule_link = models.URLField(max_length=255,blank=True)
	change_date = models.DateField(blank=True,null=True)
        
	def __unicode__(self):
		return self.route_name

class RouteForm(forms.Form):
	route = forms.CharField(max_length=25)