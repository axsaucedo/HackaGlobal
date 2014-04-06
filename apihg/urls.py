from django.conf.urls.defaults import *
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from django.http import HttpResponse
import json

from hackaglobal.models import Event

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (    'id'
                    , 'creator'
                    , 'name'
                    , 'description'
                    , 'address'
                    , 'country'
                    , 'city'
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
    def get(self, request, country, city, format=None):
        if city:
            events = Event.objects.filter(country=country, city=city)
        else:
            events = Event.objects.filter(country=country)

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


def getCountryCity(request, city):

    citycountry = {
            "Mexico" : [
                  "MexicoCity"
                , "Guadalajara"
                ,
            ]
            , "China" : [
                "Shanghai"
                ,
            ]
            , "Russia" : [
                 "Moscow"
               , "SaintPetersburg"
               ,
            ]
            , "Romania" : [
                "Timisoara"
                , "Cluj"
                , "Bucharest"
                , "Brasov"
                , "Caransebes"
                , "Arad"
                , "Iasi"
                ,
            ]
            , "UK" : [
                  "Southampton"
                , "Manchester"
                , "Sheffield"
                , "London"
            ]

    }

    if not city:
        response = citycountry.keys()
    else:
        response = citycountry[city]

    return HttpResponse(json.dumps(response), content_type="application/json")


handler404 = 'hackaglobal.views.handler404'

urlpatterns = patterns('',
    url(r'^data/$', EventList.as_view()),
    url(r'^data/(?P<country>\w+)(/(?P<city>\w+))?/$', EventFilteredList.as_view()),
    url(r'^event/(?P<pk>[0-9]+)/$', EventDetail.as_view()),
    url(r'^country/(?P<city>.*)$', getCountryCity, name="country-list"),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
