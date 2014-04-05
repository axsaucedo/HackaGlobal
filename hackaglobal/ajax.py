from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from hackaglobal.tools.toolbox import  send_async_mail

import json

from hackaglobal.models import Event, Attendee, Staff
from django.contrib.auth.models import User

import logging

@login_required
@require_POST
def attend_event(request):
    response = {}

    try:
        event_id = request.POST["event_id"]
        attendee_type = request.POST['attendee_type']

        event = Event.objects.get(id=event_id)

        if attendee_type != "" and not Attendee.objects.filter(attendee=request.user, event=event).exists():
            attendee = Attendee()
            attendee.attendee = request.user
            attendee.event = event
            attendee.type = attendee_type

            attendee.save()

            to = [event.creator.username]
            for attendee in event.attendee_set.all():
                if not to.__contains__(attendee.attendee.username):
                    to.append(attendee.attendee.username)

            msg = EmailMultiAlternatives()
            msg.from_email = "hackasoton@gmail.com"
            msg.to = to
            msg.subject = "New Attendee!"

            body = "<a href='http://events-finder.appspot.com/accounts/view/" + request.user.username + "'>" + request.user.first_name + " " + request.user.last_name + "</a> is now " + ('attending' if attendee_type == 'A' else 'tracking') + " the event <a href='http://events-finder.appspot.com/event/" + event_id + "'>" + event.name + "</a>!"
            msg.body = body
            msg.attach_alternative(body, 'text/html')
            send_async_mail(msg)

        else:
            attendee_instance = Attendee.objects.get(attendee=request.user, event=event)
            attendee_instance.delete()

    except Exception, err:
        response['error'] = err.__str__()

    return HttpResponse(json.dumps(response), content_type="application/json")



@login_required
@require_POST
def add_staff(request):
    response = {}

    try:
        event_id = request.POST["event_id"]
        staff_type = request.POST['staff_type']
        username = request.POST['username']
        name = request.POST['name']
        url = request.POST['url']
        imgurl = request.POST['imgurl']

        event = Event.objects.get(id=event_id)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        staff = Staff()
        staff.staff = user
        staff.name = name
        staff.url = url
        staff.event = event
        staff.type = staff_type
        staff.imgurl = imgurl

        staff.save()


        to = [event.creator.username]
        for attendee in event.attendee_set.all():
            if not to.__contains__(attendee.attendee.username):
                to.append(attendee.attendee.username)

        msg = EmailMultiAlternatives()
        msg.from_email = "hackasoton@gmail.com"
        msg.to = to
        msg.subject = "New Attendee!"

        body = "A new " + ("Organizer" if staff_type == "O" else ("Speaker" if staff_type == "S" else "Mentor")) + " has been added to the event <a href='http://events-finder.appspot.com/event/" + event_id + "'>" + event.name + "</a>!"
        msg.body = body
        msg.attach_alternative(body, 'text/html')
        send_async_mail(msg)

        response['staff_id'] = staff.id

    except Exception, err:
        response['error'] = err.__str__()

    return HttpResponse(json.dumps(response), content_type="application/json")



@login_required
@require_POST
def remove_staff(request):
    response = {}

    try:
        staff_id = request.POST["staff_id"]

        staff = Staff.objects.get(id=staff_id)
        staff.delete()

    except Exception, err:
        response['error'] = err.__str__()

    return HttpResponse(json.dumps(response), content_type="application/json")
