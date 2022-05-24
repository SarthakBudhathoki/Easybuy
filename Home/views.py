from itertools import product
from django.shortcuts import redirect, render
from .models import Product


def home(request):

    return render(request,'home/home.html',)

def categorie(request):

    return render(request,'productpage/categorie.html',)


def productpage(request):
    context  = {
        'products':Product.objects.all(),
        }
    
   
    return render(request,'productpage/productpage.html',context)

def SearchView(request):
    query = request.GET['query']
    products = Product.objects.filter(name__icontains =query)
    context ={ 'products':products}
    return render(request,'productpage/search.html',context)    

def searchresult(request):
    query = request.GET['query']
    products = Product.objects.filter(name__icontains =query)
    context ={ 'products':products}
    return render(request,'productpage/search.html',context)  

def edit(request, id):
   numbers = Product.objects.get(id=id)
   products = Product.objects.all()
   context  = {
        'products': products,'numbers' : numbers
      }

   return render(request,'productpage/edit.html',context)

def contact(request):
    return render(request, 'contact/contact.html')

def signuplogin(request):
    return render(request, 'Account/signuplogin.html')
   