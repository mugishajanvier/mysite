import pywapi
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from .form import Cityform
from .models import WeatherCondition


# Create your views here.
def weather(request):
    less='null'
    form=Cityform(request.POST or None)
    if form.is_valid():
        city=form.cleaned_data['city_name']
        lookup= pywapi.get_location_ids(city)
        for i in lookup:
          location=i
        weather_com_result = pywapi.get_weather_from_weather_com(location)
        city_name=city
        temperature=weather_com_result['current_conditions']['temperature']
        humidity=weather_com_result['current_conditions']['humidity']
        visibility=weather_com_result['current_conditions']['visibility']
        weather_obj=WeatherCondition(city_name = city_name, temperature = temperature , humidity = humidity, visibility = visibility)
        weather_obj.save()
        j=0
        temp=[]
        temp2=[]
        date=[]
        for i in weather_com_result['forecasts']:
            temp.append(i['high'])
        for i in weather_com_result['forecasts']:
            temp2.append(i['low'])
        for i in weather_com_result['forecasts']:
            date.append(i['date'])

        variables = RequestContext(request,{
    'weather_com_result' : weather_com_result,
    'city' : city,
    'form' : form,
        'j' : j,
        'temp' :temp,
        'temp2' :temp2,
        'date' :date,
        })
    else:
        variables = RequestContext(request,{
            'weather_com_result' : less,
    'form' : form,})
    return render_to_response("weather.html", variables)





