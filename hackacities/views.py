from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from hackaglobal.tools.forms import HackaCityCreationForm

from hackacities.models import HackaCity
from django.db.models import Q

import settings


def view_hackacity(request, hc):

    print hc

    if hc.lower() == "global":
        return HttpResponseRedirect(reverse('home'))

    try:
        print "here"
        hackacity = HackaCity.objects.get(name=hc)

    except HackaCity.DoesNotExist:
        try:
            if hc.isdigit():
                hackacity = HackaCity.objects.get(pk=hc)
                print hackacity.name
            else:
                hackacity = HackaCity.objects.get(Q(city__name=hc) | Q(name="Hacka"+hc))

            return HttpResponseRedirect(reverse('view_hackacity', args=[hackacity.name]))

        except HackaCity.DoesNotExist:
            return render(request, 'generic_message.html', { 'header' : 'HackaCity not found', 'message': "Oops, we couldn't the HackaCity you were looking for..." })

    is_hackateam = HackaCity.objects.filter(id=hackacity.pk, team=request.user).exists()

    return render(request, 'hackacity/hackacity_view.html', { 'hackacity': hackacity, 'is_hackateam':True })


def edit_hackacity(request, hc):

    data = {}
    data['form'] = request.POST.get("form", "")

    try:
        if hc.isdigit():
            data['hackacity'] = HackaCity.objects.get(pk=hc, team=request.user)
        else:
            data['hackacity'] = HackaCity.objects.get(Q(name=hc) | Q(city__name=hc), team=request.user)

    except:
        return render(request, 'generic_message.html', { 'header' : 'HackaCity not found', 'message': "Oops, we couldn't the HackaCity you were looking for..." })


    try:

        if request.method =='POST':
            data['form'] = HackaCityCreationForm(request.POST, request.FILES)

            # Check if form is valid and if the user is part of the event hackacity's team
            if data['form'].is_valid():
                new_hackacity = data['form'].save(commit=False)
                new_hackacity.id = data['hackacity'].id
                new_hackacity.name = data['hackacity'].name
                new_hackacity.city = data['hackacity'].city
                new_hackacity.lead = data['hackacity'].lead

                if not new_hackacity.image_logo: new_hackacity.image_logo = data['hackacity'].image_logo
                if not new_hackacity.image_about: new_hackacity.image_about = data['hackacity'].image_about
                if not new_hackacity.image_home: new_hackacity.image_home = data['hackacity'].image_home
                if not new_hackacity.image_divider_1: new_hackacity.image_divider_1 = data['hackacity'].image_divider_1
                if not new_hackacity.image_divider_2: new_hackacity.image_divider_2 = data['hackacity'].image_divider_2
                if not new_hackacity.image_divider_3: new_hackacity.image_divider_3 = data['hackacity'].image_divider_3
                if not new_hackacity.image_divider_4: new_hackacity.image_divider_4 = data['hackacity'].image_divider_4

                new_hackacity.save()

                data['hackacity'] = new_hackacity
        else:
            data['form'] = HackaCityCreationForm()

    except Exception, err:
        # Event not found so raise an event not found
        return render(request, 'generic_message.html', { 'header' : 'Event not found...', 'message': err if settings.DEBUG else "Oops, we couldn't find the event you were looking for..." })


    data['is_lead'] = data['hackacity'].lead == request.user

    return render(request, 'hackacity/hackacity_edit.html', data)