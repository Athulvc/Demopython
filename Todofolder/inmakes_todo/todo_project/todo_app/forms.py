from django import forms
from django.forms import ModelForm
from. models import tasks1

from.models import tasks1

class Todoform(forms.ModelForm):
    class Meta:
        model=tasks1
        fields=['name','priority','date']