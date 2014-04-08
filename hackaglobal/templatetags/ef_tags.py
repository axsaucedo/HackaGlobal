from django import template
from hackaglobal.models import Event, Attendee
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
def all_tags():

    all_tags_set = set()
    for event in Event.objects.all():
        all_tags_set |= set(tuple(event.tags))

    all_tags = list(all_tags_set)

    return all_tags

@register.assignment_tag()
def split(value):
    return value.split(',')


@register.assignment_tag()
def base_url():
    return BASE_URL

@register.assignment_tag()
def in_prod():
    return not DEBUG