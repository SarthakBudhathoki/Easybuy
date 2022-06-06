from unittest import result
from django.urls import reverse,resolve
from django.test import SimpleTestCase
from Home.views import  home, productpage, SearchView, searchresult, edit
# Create your tests here.
class TestUrls(SimpleTestCase):

      # For blog
    def test_case_blog_url(self):
        url=reverse('blog')
        self.assertEquals(resolve(url).func,edit)

    # For blog_detail
    def test_case_blog_detail_url(self):
        url=reverse('blog_detail')
        self.assertEquals(resolve(url).func,edit)

      # For categorie
    def test_case_categorie_detail_url(self):
        url=reverse('categorie')
        self.assertEquals(resolve(url).func,edit)
    
    # For signuplogin
    def test_case_signuplogin_detail_url(self):
        url=reverse('signuplogin')
        self.assertEquals(resolve(url).func,edit)

    # For contact
    def test_case_contact_detail_url(self):
        url=reverse('contact')
        self.assertEquals(resolve(url).func,edit)
    