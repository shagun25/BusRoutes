from django.contrib import admin
from .models import TransportCompany, Bus, Stop, Route, Schedule, RouteStop

@admin.register(TransportCompany)
class TransportCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_information')

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('number', 'model', 'capacity', 'company')

@admin.register(Stop)
class StopAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('starting_stop', 'destination_stop')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('departure_time', 'arrival_time', 'bus', 'route')

@admin.register(RouteStop)
class RouteStopAdmin(admin.ModelAdmin):
    list_display = ('route', 'stop')
