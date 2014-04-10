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

class Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35L)
    country_code = models.CharField(max_length=3L)
    district = models.CharField(max_length=20L)
    population = models.IntegerField()

class Countries(models.Model):
    code = models.CharField(max_length=3L, primary_key=True)
    name = models.CharField(max_length=52L)
    continent = models.CharField(max_length=13L)
    region = models.CharField(max_length=26L)
    surface_area = models.FloatField()
    independence_year = models.IntegerField(null=True, blank=True)
    population = models.IntegerField()
    life_expectancy = models.FloatField(null=True, blank=True)
    gnp = models.FloatField(null=True, blank=True)
    gnp_old = models.FloatField(null=True, blank=True)
    local_name = models.CharField(max_length=45L)
    government_form = models.CharField(max_length=45L)
    head_of_state = models.CharField(max_length=60L, blank=True)
    capital = models.IntegerField(null=True, blank=True)
    code2 = models.CharField(max_length=2L)

class Languages(models.Model):
    country_code = models.CharField(max_length=3)
    language = models.CharField(max_length=30)
    official = models.CharField(max_length=1)
    percentage = models.FloatField()