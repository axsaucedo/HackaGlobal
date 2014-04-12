from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


CONTAINER_TYPE_CHOICES = (
        ('G', 'Gold Sponsor'),
        ('S', 'Silver Sponsor'),
        ('B', 'Bronze Sponsor'),
        ('P', 'Partner'),
        ('C', 'Community'),
    )

class HackaContainer(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='profiles/')
    url = models.URLField()

    type = models.CharField(max_length=1, choices=CONTAINER_TYPE_CHOICES, default='C')

class HackaCity(models.Model):
    lead = models.ForeignKey(User, related_name="lead_of")
    team = models.ManyToManyField(User, related_name="team_of", null=True, blank=True)
    member = models.ManyToManyField(User, related_name="member_of", null=True, blank=True)

    photo = models.ImageField(upload_to='profiles/')

    name = models.CharField(max_length=25)
    short_description = models.CharField(max_length=200)
    about = models.TextField()
    city = models.OneToOneField('Cities')

    sponsors = models.ForeignKey(HackaContainer, related_name="sponsor_of", null=True, blank=True)
    communities = models.ForeignKey(HackaContainer, related_name="community_of", null=True, blank=True)
    partners = models.ForeignKey(HackaContainer, related_name="partner_of", null=True, blank=True)

    def image_tag(self):
        return u'<img src="%s" />' % (self.photo.url if self.photo else '/static/home/img/full_logo.png')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.city.name

class Cities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35L)
    country_code = models.CharField(max_length=3L)
    district = models.CharField(max_length=20L)
    population = models.IntegerField()
    country = models.ForeignKey('Countries')

    def __unicode__(self):
        return self.name

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

    def __unicode__(self):
        return self.name

class Languages(models.Model):
    country = models.ForeignKey('Countries')
    country_code = models.CharField(max_length=3)
    language = models.CharField(max_length=30)
    official = models.CharField(max_length=1)
    percentage = models.FloatField()

    def __unicode__(self):
        return self.language