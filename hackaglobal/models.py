from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

from taggit.managers import TaggableManager


ATTENDEE_TYPE_CHOICES = (
        ('A', 'Attendee'),
        ('T', 'Tracker'),
    )

STAFF_TYPE_CHOICES = (
        ('O', 'Organizer'),
        ('S', 'Speaker'),
        ('M', 'Mentor'),
    )

CONTAINER_TYPE_CHOICES = (
        ('G', 'Gold Sponsor'),
        ('S', 'Silver Sponsor'),
        ('B', 'Bronze Sponsor'),
        ('P', 'Partner'),
        ('C', 'Community'),
    )


# TODO add sponsors!!
class Event(models.Model):
    creator = models.ForeignKey(User, unique=False)
    name = models.CharField(_("Event Name"), max_length=50)
    description = models.TextField(_("Event Description"), null=True, blank=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    website = models.URLField(null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    tags = TaggableManager()

    def get_address_array(self):
        return [ self.address, self.country, self.city, self.zip ]

    def get_short_address(self):
        return self.zip + " " + self.city + ", " + self.country

    def get_creator(self):
        return self.creator

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


class HackaContainer(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='profiles/')
    url = models.URLField()

    type = models.CharField(max_length=1, choices=CONTAINER_TYPE_CHOICES, default='C')

class HackaCity(models.Model):
    lead = models.ForeignKey(User, related_name="lead_of", unique=True)
    team = models.ManyToManyField(User, related_name="team_of", null=True, blank=True)
    member = models.ManyToManyField(User, related_name="member_of", null=True, blank=True)

    photo = models.ImageField(upload_to='profiles/')

    name = models.CharField(max_length=25)
    short_description = models.CharField(max_length=200)
    about = models.TextField()
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)

    sponsors = models.ForeignKey(HackaContainer, related_name="sponsor_of", null=True, blank=True)
    communities = models.ForeignKey(HackaContainer, related_name="community_of", null=True, blank=True)
    partners = models.ForeignKey(HackaContainer, related_name="partner_of", null=True, blank=True)

#class City(models.Model):
#    name = models.CharField(max_length=35)
#    country_code = models.CharField(max_length=3)
#    district = models.CharField(max_length=20)
#    population = models.IntegerField(max_length=11, default=0)
#
#class Country(models.Model):
#    code = models.CharField(max_length=3, primary_key=True)
#    name = models.CharField(max_length=52)
#    continent
