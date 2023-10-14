from django import forms
from .models import *

class Creation(forms.ModelForm):
    class Meta:
        model = Topic
        fields ='__all__'
        