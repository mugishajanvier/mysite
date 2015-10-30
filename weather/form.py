from django import forms

class Cityform(forms.Form):
    city_name=forms.CharField(label=u'City Name', max_length=30)