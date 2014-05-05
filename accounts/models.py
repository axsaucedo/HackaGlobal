from django.db import models
from django.contrib.auth.models import User
from hackaglobal.tools.toolbox import  path_and_rename

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    photo = models.ImageField(upload_to=path_and_rename('profiles/', u'profile'), null=True, blank=True)

    github = models.URLField(null=True, blank=True, default="")
    linkedin = models.URLField(null=True, blank=True, default="")
    twitter = models.URLField(null=True, blank=True, default="")
    facebook = models.URLField(null=True, blank=True, default="")
    title = models.CharField(max_length=50, null=True, blank=True, default="")
    description = models.CharField(max_length=200, null=True, blank=True, default="")

    def get_photo(self): return self.photo.url if self.photo else '/media/profiles/placeholder.jpg'
    def image_tag(self): return u'<img src="%s" />' % self.get_photo()
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return "%s's profile" % self.user

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

# This function will create a UserProfile whenever a User is created
from django.db.models.signals import post_save
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)