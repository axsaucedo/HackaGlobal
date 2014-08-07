from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from hackaglobal.tools.toolbox import  send_async_mail
from hackaglobal.tools.forms import HackaContainerCreationForm

import json

from hackaglobal.models import Event, Attendee
from hackacities.models import HackaContainer, HackaCity
from django.contrib.auth.models import User


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
def add_container(request):
    response = {}

#    if True:
#        new_hc = HackaContainer.objects.all()[0]
#        response['hc'] = {
#            "id": new_hc.id
#            , "title": new_hc.title
#            , "url": new_hc.url
#            , "photo": new_hc.photo.url
#            , "type": new_hc.type
#        }
#        return HttpResponse(json.dumps(response), content_type="application/json")

    try:
        #Check if user has right to add sponsor
        if not HackaCity.objects.get(id=request.POST['hackacity']).team.all().filter(id=request.user.id).exists():
            raise Exception("User is not allowed to add sponsor")

#        print request.POST['form']
        print request.FILES
        hc_form = HackaContainerCreationForm(request.POST, request.FILES)

        if hc_form.is_valid():
            hc = hc_form.save()
            response['hc'] = {
                  "id": hc.id
                , "title": hc.title
                , "url": hc.url
                , "photo": hc.photo.url
                , "type": hc.type
            }
        else:
            print hc_form.errors
            raise Exception("Not Valid")

    except Exception, err:
        print "ERROR"
        print err
        response['error'] = err.__str__()

    return HttpResponse(json.dumps(response), content_type="application/json")



@login_required
@require_POST
def remove_container(request):
    response = {}
    print request.POST

    try:
        container_id = request.POST["container_id"]

        container = HackaContainer.objects.get(id=container_id)
        container.delete()

    except Exception, err:
        response['error'] = err.__str__()

    return HttpResponse(json.dumps(response), content_type="application/json")

@login_required
@require_POST
def add_team(request):
    response = {}

    try:
        username = request.POST["username"]
        hackacity = request.POST["hackacity"]

        teammate = User.objects.get(username=username)
        hc = HackaCity.objects.get(name=hackacity)

        if hc.team.filter(username=username):
            raise Exception("User is already in team.")

        hc.team.add(teammate)

        response['team'] = {
            "username": teammate.username
            , "photo": teammate.profile.get_photo()
            , "name": teammate.profile.get_full_name()
        }

    except Exception, err:
        response['error'] = err.__str__()

    return HttpResponse(json.dumps(response), content_type="application/json")

@login_required
@require_POST
def remove_team(request):
    response = {}

    try:
        username = request.POST["username"]
        hackacity = request.POST["hackacity"]

        teammate = User.objects.get(username=username)
        hc = HackaCity.objects.get(name=hackacity)

        hc.team.remove(teammate)

    except Exception, err:
        response['error'] = err.__str__()

    return HttpResponse(json.dumps(response), content_type="application/json")
