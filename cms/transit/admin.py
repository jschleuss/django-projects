from django.contrib import admin
from apps.transit.models import Route

class RouteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'description', 'change')
    list_filter = ('change',)
    search_fields = ['route_name','description']

    def queryset(self, request):
        qs = super(RouteAdmin, self).queryset(request)
        qs = qs.extra(
            select={'route_int': 'CAST(route_number AS INTEGER)'}
        ).order_by('route_int')
        return qs
    

admin.site.register(Route, RouteAdmin)
