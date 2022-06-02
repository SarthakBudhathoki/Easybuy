from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponseRedirect
from .models import Product, Blogs
from django.contrib.auth import   get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import  View
from .models import *

def home(request):

    return render(request,'home/home.html',)



def login(request):

    return render(request,'Account/signuplogin.html',)

def categorie(request):

    return render(request,'productpage/categorie.html',)   

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

class Index(View):
    
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();

        data = {}
        data['products'] = products
        data['categories'] = categories

        print('you are : ', request.session.get('email'))
        return render(request, 'productpage/productpage.html', data)

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )

def edit(request, id):
   numbers = Product.objects.get(id=id)
   products = Product.objects.all()
   context  = {
        'products': products,'numbers' : numbers
      }

   return render(request,'productpage/edit.html',context)

def contact(request):
    return render(request, 'contact/contact.html')


# class CheckOut(View):
#     def post(self, request):
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         customer = request.session.get('customer')
#         cart = request.session.get('cart')
#         products = Product.get_products_by_id(list(cart.keys()))
#         print(address, phone, customer, cart, products)

#         for product in products:
#             print(cart.get(str(product.id)))
#             order = Order(customer=Customer(id=customer),
#                           product=product,
#                           price=product.price,
#                           address=address,
#                           phone=phone,
#                           quantity=cart.get(str(product.id)))
#             order.save()
#         request.session['cart'] = {}

#         return redirect('cart')


class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})


