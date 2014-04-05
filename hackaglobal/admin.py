from django.contrib.admin import site, ModelAdmin
from hackaglobal.models import Event, Attendee, Staff

def tags(instance):
    return ', '.join(instance.tags)

class EventAdmin(ModelAdmin):
    list_display = ['name', 'description', 'creator', 'latitude', 'longitude', 'start', 'end', 'get_short_address', tags]


site.register(Event, EventAdmin)
site.register(Attendee)
site.register(Staff)
