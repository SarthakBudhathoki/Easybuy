from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static
from .middlewares.auth import  auth_middleware
from .views import  *

urlpatterns = [
    path('home', views.home ,name="home"),
    path('', productpage.as_view(), name='productpage'),
    path('store', store , name='store'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('delete_cart/<int:id>',delete_cart,name='delete_cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('categorie', views.categorie,name="categorie"),
    path('login', Login.as_view(), name='login'),
    # path('creatorlogin', creatorlogin.as_view(), name='creatorlogin'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout', views.logout , name='logout'),
    path('profile', views.profile , name='profile'),
    path('edit/<int:id>', views.edit ,name="edit"),
    path('contact', views.contact, name='contact'),
    path("search/", views.SearchView, name="search"),
    path("searchresult/", views.searchresult, name="searchresult"),
    path('blog/', views.showblog, name='blog'),
    path('creatorlogin', views.creatorlogin, name="creatorlogin"),
    path('<int:id>', views.blog_detail, name='blog_detail'),
    path('livechat', views.livechat, name= 'livechat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send,name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)