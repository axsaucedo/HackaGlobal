from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from hackaglobal.models import Event, Attendee, Staff
from django.http import HttpResponseRedirect
import settings

from hackaglobal.tools.forms import EventCreationForm

def home(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def add_event(request):

    if request.method =='POST':
        form = EventCreationForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            if request.POST['tags']: event.tags.add(*request.POST['tags'].split(','))
            event.save()
            return redirect('manage_events')
    else:
        form = EventCreationForm()

    return render(request, 'add_event.html', { 'form' : form, 'debug' : False })

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def manage_events(request):
    created = Event.objects.filter(creator=request.user)
    attendee_all = Attendee.objects.filter(attendee=request.user)
    attending = []
    for a in attendee_all:
        attending.append(a.event)

    return render(request, 'manage_events.html', { 'created': created, 'attending': attending })

def edit_event(request, event_id):

    data = {}
    data['form'] = request.POST.get("form", "")

    try:
        data['event'] = Event.objects.get(id=event_id)

        if data['event'].creator != request.user:
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

            if data['form'].is_valid():
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

        if event.creator != request.user:
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