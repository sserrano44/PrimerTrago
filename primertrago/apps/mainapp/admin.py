from django.contrib import admin
from mainapp.models import Bar, Neighborhood, City, HappyHour, SubNeighborhood


class HappyHourInline(admin.TabularInline):
    model = HappyHour

class BarAdmin(admin.ModelAdmin):
    inlines = [
        HappyHourInline,
    ]

admin.site.register(Bar, BarAdmin)
admin.site.register(Neighborhood)
admin.site.register(SubNeighborhood)
admin.site.register(City)
