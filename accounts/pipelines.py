from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend

from urllib2 import urlopen, HTTPError
from uuid import uuid4
from django.core.files.base import ContentFile
from django.utils.text import slugify

def get_user_avatar(backend, details, response, social_user, uid,user, *args, **kwargs):
    url = None
    profile = user.get_profile()
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