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