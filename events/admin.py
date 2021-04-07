from django.contrib import admin
from .models import Event,EventSpecifics


# inline class for event specifics 
class EventSpecificsInline( admin.StackedInline):
    model = EventSpecifics

class EventAdmin( admin.ModelAdmin):
    inlines = [ EventSpecificsInline , ]


# admin.site.register( EventAdmin, Event )
admin.site.register(Event)
admin.site.register( EventSpecifics)
