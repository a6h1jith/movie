from django import forms
from .models import film

class updated(forms.ModelForm):
    class Meta:
        model=film
        fields=['name','desc','year','img']

