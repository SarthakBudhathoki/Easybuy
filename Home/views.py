from itertools import product
from django.shortcuts import redirect, render
from .models import Product



def homepage(request):
    context  = {
        'products':Product.objects.all(),
        }
    
   
    return render(request,'Navbar/homepage.html',context)

def edit(request, id):
   numbers = Product.objects.get(id=id)
   products = Product.objects.all()
   context  = {
        'products': products,'numbers' : numbers
      }
   return render(request,'Navbar/edit.html',context)

def contact(request):
    return render(request, 'contact/contact.html')