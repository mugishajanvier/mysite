from django.db import models

# Create your models here.
class WeatherCondition(models.Model):
    city_name = models.CharField(max_length=64)
    temperature = models.CharField(max_length=3)
    humidity = models.CharField(max_length=3)
    visibility = models.CharField(max_length=3)
    timestamp = models.DateTimeField(auto_now_add = True,auto_now = False)
    def __unicode__(self):
        return self.city_name
