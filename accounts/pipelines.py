from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend

from urllib2 import urlopen, HTTPError
from uuid import uuid4
from django.core.files.base import ContentFile
from django.utils.text import slugify

def get_user_avatar(backend, details, response, social_user, uid,user, *args, **kwargs):
    url = None
    profile = user.profile
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

    elif backend.__class__ == TwitterBackend:
        url = response.get('profile_image_url', '').replace('_normal', '')

    if url:
        try:
            avatar = urlopen(url)
            rstring = uuid4().get_hex()
            fname = slugify(unicode(rstring) + u'_p') + u'.jpg'
            profile.photo.save(fname,
                ContentFile(avatar.read()))
            profile.save()
        except HTTPError:
            pass

#from social_auth.backends.facebook import FacebookBackend
#from social_auth.backends import google
#from social_auth.signals import pre_update
#
#def social_extra_values(sender, user, response, details, **kwargs):
#    result = False
#
#    if "id" in response:
#        from accounts.models import UserProfile
#        from urllib2 import urlopen, HTTPError
#        from django.template.defaultfilters import slugify
#        from django.core.files.base import ContentFile
#
#        try:
#            url = None
#            profile = user.get_profile()
#            if sender == FacebookBackend:
#                url = "http://graph.facebook.com/%s/picture?type=large"\
#                      % response["id"]
#            elif sender == google.GoogleOAuth2Backend and "picture" in response:
#                url = response["picture"]
#
#            if url:
#                avatar = urlopen(url)
#                rstring = uuid4().get_hex()
#                fname = slugify(unicode(rstring) + u'_p') + u'.jpg'
#                profile.profile_photo.save(fname,
#                    ContentFile(avatar.read()))
#                profile.save()
#
#        except HTTPError:
#            pass
#
#        result = True
#
#    return result
#
#pre_update.connect(social_extra_values, sender=None)