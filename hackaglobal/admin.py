from django.contrib.admin import site, ModelAdmin
from hackaglobal.models import Event, Attendee, Staff, Subdomain
from hackacities.models import HackaCity, HackaContainer
from accounts.models import UserProfile


class HackaCityAdmin(ModelAdmin):
    list_display = ['city', 'lead', 'name', 'short_description']

class EventAdmin(ModelAdmin):
    list_display = ['name', 'description', 'latitude', 'longitude', 'start', 'end', 'get_city', 'get_tags']


site.register(Event, EventAdmin)

site.register(Attendee)
site.register(Staff)
site.register(Subdomain)

site.register(UserProfile)

site.register(HackaCity, HackaCityAdmin)
site.register(HackaContainer)
