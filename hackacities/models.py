from django.db import models

from django.contrib.auth.models import User
from hackaglobal.tools.toolbox import  path_and_rename
from django.utils.translation import ugettext as _


CONTAINER_TYPE_CHOICES = (
        ('S1', 'Gold Sponsor'),
        ('S2', 'Silver Sponsor'),
        ('S3', 'Bronze Sponsor'),
        ('P1', 'Partner'),
        ('P2', 'Media Partner'),
    )

class HackaContainer(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=path_and_rename('hackacities/sponsors/', u'sponsor'))
    url = models.URLField()
    hackacity = models.ForeignKey("HackaCity", null=True, blank=True)

    type = models.CharField(max_length=2, choices=CONTAINER_TYPE_CHOICES, default='S1')

    def __unicode__(self):
        return self.title + ": " + self.type + " - " + self.hackacity.name

class HackaCity(models.Model):
    lead = models.ForeignKey(User, related_name="lead_of")
    team = models.ManyToManyField(User, related_name="team_of", null=True, blank=True)
    member = models.ManyToManyField(User, related_name="member_of", null=True, blank=True)

    image_logo = models.ImageField(upload_to=path_and_rename('hackacities/logos/', u'logo'))
    image_home = models.ImageField(upload_to=path_and_rename('hackacities/home/', u'home'), null=True, blank=True)
    image_about = models.ImageField(upload_to=path_and_rename('hackacities/about/', u'about'), null=True, blank=True)
    image_divider_1 = models.ImageField(upload_to=path_and_rename('hackacities/dividers/', u'divider'), null=True, blank=True)
    image_divider_2 = models.ImageField(upload_to=('hackacities/dividers/', u'divider'), null=True, blank=True)
    image_divider_3 = models.ImageField(upload_to=path_and_rename('hackacities/dividers/', u'divider'), null=True, blank=True)
    image_divider_4 = models.ImageField(upload_to=path_and_rename('hackacities/dividers/', u'divider'), null=True, blank=True)

    name = models.CharField(max_length=25)
    short_description = models.CharField(max_length=200)
    about = models.TextField()
    city = models.OneToOneField('Cities')

#    sponsors = models.ForeignKey(HackaContainer, related_name="sponsor_of", null=True, blank=True)
#    communities = models.ForeignKey(HackaContainer, related_name="community_of", null=True, blank=True)
#    partners = models.ForeignKey(HackaContainer, related_name="partner_of", null=True, blank=True)

    def image_tag(self): return u'<img src="%s" />' % (self.photo.url if self.photo else '/static/home/img/full_logo.png')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def get_hacka(self): return self.name.replace("Hacka","")

    def get_image_home(self): return self.image_home.url if self.image_home else '/static/defaultmedia/default-hackacity-home.jpg'
    def get_image_about(self): return self.image_about.url if self.image_about else '/static/defaultmedia/default-hackacity-about.png'
    def get_image_divider_1(self): return self.image_divider_1.url if self.image_divider_1 else '/static/defaultmedia/default-hackacity-divider-1.png'
    def get_image_divider_2(self): return self.image_divider_2.url if self.image_divider_2 else '/static/defaultmedia/default-hackacity-divider-2.jpg'
    def get_image_divider_3(self): return self.image_divider_3.url if self.image_divider_3 else '/static/defaultmedia/default-hackacity-divider-3.png'
    def get_image_divider_4(self): return self.image_divider_4.url if self.image_divider_4 else '/static/defaultmedia/default-hackacity-divider-4.jpg'

    def __unicode__(self):
        return self.city.name

class Cities(models.Model):
    name = models.CharField(max_length=35L)
    country = models.ForeignKey('Countries')

    def __unicode__(self):
        return self.name

class Countries(models.Model):
    code = models.CharField(max_length=3L, primary_key=True)
    name = models.CharField(max_length=52L)
    continent = models.CharField(max_length=13L)

    def __unicode__(self):
        return self.name

#
#class Cities(models.Model):
#    id = models.IntegerField(primary_key=True)
#    name = models.CharField(max_length=35L)
#    country_code = models.CharField(max_length=3L)
#    district = models.CharField(max_length=20L)
#    population = models.IntegerField()
#    country = models.ForeignKey('Countries')
#
#    def __unicode__(self):
#        return self.name
#
#class Countries(models.Model):
#    code = models.CharField(max_length=3L, primary_key=True)
#    name = models.CharField(max_length=52L)
#    continent = models.CharField(max_length=13L)
#    region = models.CharField(max_length=26L)
#    surface_area = models.FloatField()
#    independence_year = models.IntegerField(null=True, blank=True)
#    population = models.IntegerField()
#    life_expectancy = models.FloatField(null=True, blank=True)
#    gnp = models.FloatField(null=True, blank=True)
#    gnp_old = models.FloatField(null=True, blank=True)
#    local_name = models.CharField(max_length=45L)
#    government_form = models.CharField(max_length=45L)
#    head_of_state = models.CharField(max_length=60L, blank=True)
#    capital = models.IntegerField(null=True, blank=True)
#    code2 = models.CharField(max_length=2L)
#
#    def __unicode__(self):
#        return self.name
#
#class Languages(models.Model):
#    country = models.ForeignKey('Countries')
#    country_code = models.CharField(max_length=3)
#    language = models.CharField(max_length=30)
#    official = models.CharField(max_length=1)
#    percentage = models.FloatField()
#
#    def __unicode__(self):
#        return self.language