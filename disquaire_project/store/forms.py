from django import forms
from .models import Artist, Album, Booking

class SearchForm(forms.Form):
    query = forms.CharField()

