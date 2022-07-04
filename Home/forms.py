from itertools import product
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

<<<<<<< HEAD

class Products(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("__all__") 
=======
class BlogForm(forms.ModelForm): 
    class Meta:
        model = Blogs
        fields = ["blog_name","blog_details","blog_image"]     

class ProductForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields = ("__all__")
>>>>>>> 3820a9d84e32c58c4a054433ca9969061bacde53
