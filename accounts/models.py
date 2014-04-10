from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    photo = models.ImageField(upload_to='profiles/')

    def image_tag(self):
        return u'<img src="%s" />' % self.photo.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return "%s's profile" % self.user

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])