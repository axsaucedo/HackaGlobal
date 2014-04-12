from django.conf.urls.defaults import *
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from django.http import HttpResponse
import json

from hackaglobal.models import Event
from hackacities.models import HackaCity, Countries, Cities

class EventListSerializer(serializers.ModelSerializer):
    country = serializers.Field(source='get_country')
    city = serializers.Field(source='get_city')

    class Meta:
        model = Event
        fields = (    'id'
                    , 'hackacity'
                    , 'name'
                    , 'description'
                    , 'address'
                    , 'country'
                    , 'city'
                    , 'website'
                    , 'start'
                    , 'end')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event

class EventList(APIView):
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)

class EventFilteredList(APIView):
    def get(self, request, countrycity, format=None):

        clean_countrycity = countrycity.replace('-',' ')

        events = Event.objects.filter(hackacity__city__name=clean_countrycity)

        if not events:
            events = Event.objects.filter(hackacity__city__country__name=clean_countrycity)

        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)

class EventDetail(APIView):

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

class EventTags(APIView):

    def get(self, request, tags):
        all_tags = tags.split(',')
        events = Event.objects.filter(tags__name__in=all_tags).distinct()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)

def getCountryCity(request, country):

    if not country:
        response = list(HackaCity.objects.values_list('city__country__name', flat="True").distinct())
    else:
        response = list(HackaCity.objects.filter(city__country__name=country).values_list('city__name', flat="True"))

    return HttpResponse(json.dumps(response), content_type="application/json")

def getTags(request, tags):
    all_tags = tags.split(',')


handler404 = 'hackaglobal.views.handler404'

urlpatterns = patterns('',

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^data/$', EventList.as_view()),
    url(r'^data/(?P<countrycity>.+)/$', EventFilteredList.as_view()),
    url(r'^event/(?P<pk>[0-9]+)/$', EventDetail.as_view()),
    url(r'^country/(?P<country>.*)$', getCountryCity, name="country-list"),


    url(r'^tags/(?P<tags>.*)/$', EventTags.as_view(), name="tag-filter"),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
