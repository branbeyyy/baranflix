from django import forms
from django.forms import ModelForm
from .models import *

class MovieForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Yeni Film Ekle...'}))
    
    class Meta:
        model = Movie
        fields = '__all__'