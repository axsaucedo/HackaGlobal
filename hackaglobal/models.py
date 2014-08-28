from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from taggit.managers import TaggableManager
from hackaglobal.tools.toolbox import  path_and_rename

from hackacities.models import HackaCity


ATTENDEE_TYPE_CHOICES = (
        ('A', 'Attendee'),
        ('T', 'Tracker'),
    )

STAFF_TYPE_CHOICES = (
        ('O', 'Organizer'),
        ('S', 'Speaker'),
        ('M', 'Mentor'),
    )


# TODO add sponsors!!
class Event(models.Model):
    hackacity = models.ForeignKey(HackaCity)
    name = models.CharField(_("Event Name"), max_length=50)
    description = models.TextField(_("Event Description"), null=True, blank=True)
    photo = models.ImageField(_("Event Photo"),upload_to=path_and_rename('hackaglobal/events/', u'event'))
    external = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=10, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    tags = TaggableManager()

    created = models.DateTimeField(auto_now=True)

    def get_photo(self):
        if not self.photo:
            return '/static/defaultmedia/default-hackaevent-photo.jpg'
        else:
            return self.photo.url

    def get_city(self):
        return self.hackacity.city.name

    def get_country(self):
        return self.hackacity.city.country.name

    def get_address_array(self):
        return [ self.address, self.hackacity.city.country_code, self.hackacity.city, self.zip ]

    def get_short_address(self):
        return self.zip + " " + self.hackacity.city.name + ", " + self.hackacity.city.country_code

    def get_tags(self):
        tags = self.tags.names()
        return ', '.join(tags)

class Attendee(models.Model):
    attendee = models.ForeignKey(User)
    type = models.CharField(max_length=1, choices=ATTENDEE_TYPE_CHOICES, default='A')
    event = models.ForeignKey(Event)

class Staff(models.Model):
    staff = models.ForeignKey(User, null=True, blank=True)

    name = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=200, null=True, blank=True)
    imgurl = models.CharField(max_length=200, null=True, blank=True)

    type = models.CharField(max_length=1, choices=STAFF_TYPE_CHOICES, default='M')
    event = models.ForeignKey(Event)


class Subdomain(models.Model):
    """A model for managing subdomains and the URLs to which they redirect."""
    name = models.SlugField(max_length=200, unique=True)
    url = models.CharField(max_length=400, verbose_name="URL")

    def __unicode__(self):
        return self.name + " - " + self.url