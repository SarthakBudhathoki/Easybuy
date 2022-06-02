from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static
from .middlewares.auth import  auth_middleware
from .views import Cart, Index, store , CheckOut, OrderView

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
     path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('categorie', views.categorie,name="categorie"),
    # path('', views.home ,name="home"),
    path('signuplogin', views.signuplogin ,name="signuplogin"),
    path('edit/<int:id>', views.edit ,name="edit"),
    path('contact', views.contact, name='contact'),
    path('signuplogin', views.signuplogin, name='signuplogin'),
    path("search/", views.SearchView, name="search"),
    path("searchresult/", views.searchresult, name="searchresult"),
    # path('blog', views.showblog, name='blog'),
    # path('blog_detail', views.blog_detail, name='blog_detail'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)