from django.contrib.auth.models import User

from app1.models import *
from rest_framework import serializers # type: ignore


class GareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gare
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']