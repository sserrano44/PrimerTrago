from django.contrib import admin
from mainapp.models import Bar, Neighborhood, City, HappyHour, SubNeighborhood


class HappyHourInline(admin.TabularInline):
    model = HappyHour

class BarAdmin(admin.ModelAdmin):
    inlines = [
        HappyHourInline,
    ]
    list_display = ('name', 'address', 'neighborhood')
    list_filter  = ('neighborhood',)
    search_fields = ('name', 'address')


admin.site.register(Bar, BarAdmin)
admin.site.register(Neighborhood)
admin.site.register(SubNeighborhood)
admin.site.register(City)
