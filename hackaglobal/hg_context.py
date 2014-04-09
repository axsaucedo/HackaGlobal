from django.conf import settings # import the settings file

def in_prod(request):
    return {"IN_PROD" : not settings.DEBUG}