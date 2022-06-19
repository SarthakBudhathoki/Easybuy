from django import forms
from .models import *

class orderform(forms.ModelForm):
    class Meta:
        model = editOrders
        fields = '__all__'