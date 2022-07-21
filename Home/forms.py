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

class BlogForm(forms.ModelForm): 
    class Meta:
        model = Blogs
        fields = ["blog_name","blog_details","blog_image"]     

class ProductForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields = ("__all__")

class ProductsForm(forms.ModelForm): 
    class Meta:
        model = Product
        fields = ["name","category","image", "description","price"]

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ("__all__")

<<<<<<< HEAD
class adminform(forms.ModelForm):
    class Meta:
        model = adminaccount
        fields = ("__all__")        
=======
class ReviewForm(forms.ModelForm): 
    class Meta:
        model = Review
        fields = ("__all__")
>>>>>>> 9d4f1bde24b5be2d6377a4ac4cbfceb47a13eabf
