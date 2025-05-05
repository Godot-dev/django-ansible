from django.contrib.auth.models import User

from app1.models import *
from rest_framework import serializers # type: ignore


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = '__all__'

class HasJourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = HasJourney
        fields = '__all__'