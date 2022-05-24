from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('productpage', views.productpage,name="productpage"),
    path('', views.home ,name="home"),
    path('signuplogin', views.signuplogin ,name="signuplogin"),
    path('edit/<int:id>', views.edit ,name="edit"),
    path('contact', views.contact, name='contact'),
    path("search/", views.SearchView, name="search"),
    path("searchresult/", views.searchresult, name="searchresult"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)