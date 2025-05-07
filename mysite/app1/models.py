from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Station(models.Model):
    station_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='stations', on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['station_id', 'owner'], name='unique_station_owner')
        ]

class Journey(models.Model):
    station1 = models.ForeignKey(Station, on_delete=models.CASCADE,  related_name="departures")
    station2 = models.ForeignKey(Station, on_delete=models.CASCADE,  related_name="arrivals")


class DetailedJourney(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    base_departure_time = models.DateField()
    departure_time = models.DateField()
    platform = models.CharField(max_length=2)

    @property
    def delay_minutes(self):
        if self.base_departure_time != self.departure_time:
            delay = self.departure_time - self.base_departure_time
            return int(delay.total_seconds() / 60)
        return 0


class HasJourney(models.Model):
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['journey', 'user'], name='unique_journey_user')
        ]

    


                                                          