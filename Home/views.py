from django.shortcuts import redirect, render
from .models import Product



def homepage(request):
    context  = {
        'products':Product.objects.all(),
        }
    
   
    return render(request,'Navbar/homepage.html',context)

def edit(request):
    image = Product.objects.all()
    
    return render(request,'Navbar/edit.html',{"image":image})