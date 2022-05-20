from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('navbar', views.navbar,name="navbar"),
    path('', views.home ,name="home"),
    path('edit/<int:id>', views.edit ,name="edit"),
  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)