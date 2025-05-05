from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Station(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='stations', on_delete=models.CASCADE, default=None, null=True)

class Journey(models.Model):
    station1 = models.ForeignKey(Station, on_delete=models.CASCADE,  related_name="departures")
    station2 = models.ForeignKey(Station, on_delete=models.CASCADE,  related_name="arrivals")
    date = models.DateField()
    platform = models.CharField(max_length=2)

class HasJourney(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    


                                                          