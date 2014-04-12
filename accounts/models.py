from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def image_tag(self):
        return u'<img src="%s" />' % (self.photo.url if self.photo else '/media/profiles/placeholder.jpg')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return "%s's profile" % self.user

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


#
#from social_auth.backends.facebook import FacebookBackend
#from social_auth.backends import google
#from social_auth.signals import socialauth_registered
#
#def new_users_handler(sender, user, response, details, **kwargs):
#
#    user.is_new = True
#    if user.is_new:
#        if "id" in response:
#
#            from urllib2 import urlopen, HTTPError
#            from django.template.defaultfilters import slugify
#            from django.core.files.base import ContentFile
#
#            try:
#                url = None
#                if sender == FacebookBackend:
#                    url = "http://graph.facebook.com/%s/picture?type=large"\
#                          % response["id"]
#                elif sender == google.GoogleOAuth2Backend and "picture" in response:
#                    url = response["picture"]
#
#                if url:
#                    avatar = urlopen(url)
#                    profile = UserProfile(user=user)
#
#                    profile.photo.save(slugify(user.username + " social") + '.jpg',
#                        ContentFile(avatar.read()))
#
#                    profile.save()
#
#            except HTTPError:
#                pass
#
#
#
#
#    return False
#
#socialauth_registered.connect(new_users_handler, sender=None)