from django import template
from hackaglobal.models import Event, Attendee
from hackacities.models import HackaCity, HackaContainer
from taggit.models import Tag
from settings import BASE_URL, DEBUG

register = template.Library()

@register.assignment_tag(takes_context=True)
def is_attending(context, event):
    user = context['request'].user

    attending = False
    try:
        attendee = Attendee.objects.get(attendee=user, event=event)
        attending = attendee.type == 'A'

    except Exception:
        pass

    return 1 if attending else 0

@register.assignment_tag(takes_context=True)
def is_tracking(context, event):
    user = context['request'].user

    tracking = False
    try:
        attendee = Attendee.objects.get(attendee=user, event=event)
        tracking = attendee.type == 'T'

    except Exception:
        pass

    return 1 if tracking else 0

@register.assignment_tag()
def get_hackacontainers(hackacity, type):

    try:
        hackacontainers = HackaContainer.objects.filter(hackacity=hackacity, type=type)
        return hackacontainers

    except Exception:
        return

@register.assignment_tag()
def all_tags():

    all_tags = []

    for tag in Tag.objects.all():
        all_tags.append(tag.name)

    return all_tags

@register.assignment_tag()
def split(value):
    return value.split(',')


@register.assignment_tag()
def base_url():
    return BASE_URL

@register.assignment_tag()
def all_hackacities_terminations_js_print():
    return ('"'+'","'.join([item for sublist in HackaCity.objects.all().values_list('city__name') for item in sublist])+'","Global"')