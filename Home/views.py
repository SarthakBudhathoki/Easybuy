from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponseRedirect, HttpResponse
from .models import Product, Blogs
from django.contrib.auth.hashers import make_password
from django.contrib.auth import   get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import  View
from .forms import *
from .models import *
from django.http import JsonResponse

def home(request):

    return render(request,'home/home.html',)


def profile(request):
    
    return render(request,'account/profile.html',)


class Signup(View):
    def get(self, request):
        return render(request, 'Account/signuplogin.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('productpage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'Account/signuplogin.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'Account/signuplogin.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('/store')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request,'Account/signuplogin.html',{'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')


def categorie(request):
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
    return render(request, 'productpage/categorie.html', data)  

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

class productpage(View):
    
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
        return redirect('productpage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        customer = Customer.objects.all()
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
        return render(request , 'productpage/cart.html' , {'products' : products} )

def edit(request, id):
    numbers = Product.objects.get(id=id)
    products = Product.objects.all()
    context  = {
        'products': products,'numbers' : numbers
      }
    print(request)
    if request.method =='POST':
        form = orderform(request.POST)
        if form.is_valid(): 
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"your order has been placed " + user)
                print(form)
        else:
            print(form)
            messages.success(request,"your order could not be placed " )
        return redirect('/')     
                

    return render(request,'productpage/edit.html',context)




def contact(request):
    return render(request, 'contact/contact.html')


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')


class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'productpage/orders.html'  , {'orders' : orders})

def delete_cart(request,id):
    cart = Cart(request)
    cart.delete(id)
    messages.error(request,"item has removed")
    context = {
            'cart':cart
          }
    return render(request,'store/cart.html',context)

def showblog(request):
    user = get_user_model()
    blogs=Blogs.objects.all()

    return render (request,"blog/blog.html",{'blogs':blogs,})

def blog_detail(request, id):
    single_blog = get_object_or_404(Blogs, pk=id)

    # usercount = User.objects.all().filter(is_superuser=False).count()
    # productcount = Products.objects.all().count()
    # productcount = Khana.objects.all().count()

    data = {
        'single_blog': single_blog,
    #     'single_blog': single_blog,
    #     'product':productcount,
       
    #     'usercount':usercount,
    #     # 'bookingcount':bookingcount,
    #     'productcount':productcount,
    }

    return render(request, 'blog/blog_detail.html', data)

  
