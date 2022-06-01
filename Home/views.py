from itertools import product
from django.shortcuts import redirect, render
from .models import Product, Blogs
from django.contrib.auth import   get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


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

<<<<<<< Updated upstream
def signuplogin(request):
    return render(request, 'Account/signuplogin.html')

def showblog(request):
    user = get_user_model()
    blogs=Blogs.objects.all()

    return render (request,"blog/blog.html",{'blogs':blogs,})

def blog_detail(request):
    # single_blog = get_object_or_404(Blogs, pk=id)
    # usercount = User.objects.all().filter(is_superuser=False).count()
    # productcount = Products.objects.all().count()
    # productcount = Khana.objects.all().count()

    # data = {
    #     'single_blog': single_blog,
    #     'product':productcount,
       
    #     'usercount':usercount,
    #     # 'bookingcount':bookingcount,
    #     'productcount':productcount,
    # }

    return render(request, 'blog/blog_detail.html')
=======

def signuplogin(request):
    return render(request, 'signuplogin/signuplogin.html')
>>>>>>> Stashed changes
   