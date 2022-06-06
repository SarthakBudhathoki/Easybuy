# Create your tests here.
from unittest import result
from django.urls import reverse,resolve
from django.test import SimpleTestCase
from Home.views import  home, productpage, SearchView, searchresult, edit
# Create your tests here.
class TestUrls(SimpleTestCase):
    
    # For login
    def test_case_login_detail_url(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,edit)

    # For contact
    def test_case_contact_detail_url(self):
        url=reverse('contact')
        self.assertEquals(resolve(url).func,edit)

      # For cart
    def test_case_cart_detail_url(self):
        url=reverse('cart')
        self.assertEquals(resolve(url).func,edit)
    
     # For check-out
    def test_case_check_out_detail_url(self):
        url=reverse('check-out')
        self.assertEquals(resolve(url).func,edit)

     # For logout
    def test_case_logout_detail_url(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func,edit)
    