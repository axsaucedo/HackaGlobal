from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from hackaglobal.models import Event, Attendee, Staff
from hackacities.models import Cities, HackaCity
from django.http import HttpResponseRedirect
import settings

from hackaglobal.tools.forms import EventCreationForm

def home(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def add_event(request):

    if request.method =='POST':
        print request.POST
        form = EventCreationForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            if request.POST['tags']: event.tags.add(*request.POST['tags'].split(','))
            event.save()
            return redirect('manage_events')
    else:
        form = EventCreationForm()

    hackacities = HackaCity.objects.filter(team=request.user)

    return render(request, 'add_event.html', { 'form' : form, 'hackacities' : hackacities })

@login_required(login_url='/accounts/login/')
def find_events(request):

    events = None

    if request.method == 'POST':
        tags = list(request.POST.get("tags", "").split(','))

        if tags:
            try:
                events = Event.objects.filter(tags__name__in=tags)

            except Exception:
                pass

    return render(request, 'find_events.html', { 'events' : events })

@login_required(login_url='/accounts/login/')
def manage_events(request):
    created = Event.objects.filter(hackacity__team=request.user)

    hackacities = HackaCity.objects.filter(team=request.user)
    attendee_all = Attendee.objects.filter(attendee=request.user)
    attending = []
    for a in attendee_all:
        attending.append(a.event)

    return render(request, 'manage_events.html', { 'hackacities': hackacities, 'created': created, 'attending': attending })

def edit_event(request, event_id):

    data = {}
    data['form'] = request.POST.get("form", "")

    try:
        data['event'] = Event.objects.get(id=event_id)

        if not data['event'].hackacity.team.filter(id=request.user.id).exists():
            return render(request, 'generic_message.html', { 'header' : 'Event not found...', 'message': "Oops, we couldn't find the event you were looking for..." })

        all_attendees = Attendee.objects.filter(event=event_id)
        all_staff = Staff.objects.filter(event=event_id)

        data['attendees'] = all_attendees.filter(type='A')
        data['trackers'] = all_attendees.filter(type='T')

        data['organizers'] = all_staff.filter(type='O')
        data['mentors'] = all_staff.filter(type='M')
        data['speakers'] = all_staff.filter(type='S')

        if request.method =='POST':
            data['form'] = EventCreationForm(request.POST)

            print request.POST['tags']

            # Check if form is valid and if the user is part of the event hackacity's team
            if data['form'].is_valid() and Event.objects.get(id=data['event'].id).hackacity.team.filter(id=request.user.id).exists():
                event = data['form'].save(commit=False)
                event.id = data['event'].id
                event.creator = request.user
                if request.POST['tags']: event.tags.add(*request.POST['tags'].split(','))
                event.save()
                data['event'] = event
        else:
            data['form'] = EventCreationForm()

    except Exception, err:
        # Event not found so raise an event not found
        return render(request, 'generic_message.html', { 'header' : 'Event not found...', 'message': err if settings.DEBUG else "Oops, we couldn't find the event you were looking for..." })

    return render(request, 'edit_event.html', data)

def delete_event(request, event_id):

    try:
        event = Event.objects.get(id=event_id)
        print event
        print event.hackacity.team.filter(id=request.user.id).exists()

        if not event.hackacity.team.filter(id=request.user.id).exists():
            return render(request, 'generic_message.html', { 'header' : 'Event not found...', 'message': "Oops, we couldn't find the event you were looking for..." })

        event.delete()

    except Exception, err:
        # Event not found so raise an event not found
        return render(request, 'generic_message.html', { 'header' : 'Event not found...', 'message': err if settings.DEBUG else "Oops, we couldn't find the event you were looking for..." })

    return HttpResponseRedirect(reverse('hackaglobal.views.manage_events'))

def view_event(request, event_id):
    data = {}

    try:
        data['event'] = Event.objects.get(id=event_id)

        all_attendees = Attendee.objects.filter(event=event_id)
        all_staff = Staff.objects.filter(event=event_id)

        data['attendees'] = all_attendees.filter(type='A')

        data['trackers'] = all_attendees.filter(type='T')

        data['organizers'] = all_staff.filter(type='O')
        data['mentors'] = all_staff.filter(type='M')
        data['speakers'] = all_staff.filter(type='S')

    except Exception, err:
        # Event not found so raise an event not found

        return render(request, 'generic_message.html', { 'header' : 'Event not found...', 'message': err if settings.DEBUG else "Oops, we couldn't find the event you were looking for..." })

    return render(request, 'view_event.html', data)

def handler404(request):
    return render(request, 'generic_message.html', { 'header' : '404 not found...', 'message': "Oops, we couldn't find what you were looking for..." })



# FrontEnd
def getCountryListView(request, country):
    return render(request, 'countrylist.html', { 'country' : country })