from django import forms
from .models import *

class orderform(forms.ModelForm):
    class Meta:
        model = editOrders
        fields = '__all__'


class Creator(forms.ModelForm):
    class Meta:
        model = signupasseller
        fields = ("__all__")     


class customers(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("__all__") 