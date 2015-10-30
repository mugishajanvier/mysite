from django.contrib import admin

# Register your models here.
from .models import WeatherCondition

class WeatherConditionAdmin(admin.ModelAdmin):

    list_display = ["__unicode__","temperature", "humidity", "visibility","timestamp"]

    class Meta :
        model= WeatherCondition


admin.site.register(WeatherCondition,WeatherConditionAdmin)
