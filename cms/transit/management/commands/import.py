from django.core.management.base import BaseCommand, CommandError
from transit.models import Route

import os, csv

def get_choice_index(index):
  if index == 'deleted':
    return '0'
  if index == 'reduced':
    return '1'
  if index == 'unchanged':
    return '2'

class Command(BaseCommand):
    def handle(self, *args, **options):
      module_dir = os.path.dirname(__file__)
      file_path = os.path.join(module_dir, 'transit.csv')
      
      with open(file_path, 'rb') as csvfile:
        transitcsv = csv.reader(csvfile, delimiter=',',quotechar='"')
        for row in transitcsv:
          try:
            print row
            route = Route.objects.get_or_create(route_name=row[0])
            route.route_name = row[0]
            route.route_number = row[1]
            route.change = get_choice_index(row[2])
            route.description = row[3]
            route.map_link = row[4]
            route.schedule_link = row[5]
            route.save()
          except:
            pass
  
            