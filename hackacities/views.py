from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from hackacities.models import HackaCity
from django.db.models import Q


def view_hackacity(request, hc):

    try:
        if hc.isdigit():
            hackacity = HackaCity.objects.get(pk=hc)
        else:
            hackacity = HackaCity.objects.get(Q(name=hc) | Q(city__name=hc))

    except HackaCity.DoesNotExist:
        return render(request, 'generic_message.html', { 'header' : 'HackaCity not found', 'message': "Oops, we couldn't the HackaCity you were looking for..." })

    return render(request, 'hackacity/hackacity_view.html', { 'hackacity': hackacity })

