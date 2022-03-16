from dataclasses import fields
from django.forms import ModelForm
from .models import Stock

class EditForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
