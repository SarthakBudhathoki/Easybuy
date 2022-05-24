from unittest import result
from django.urls import reverse,resolve
from django.test import SimpleTestCase
from Home.views import  home, productpage, SearchView, searchresult, edit
# Create your tests here.
class TestUrls(SimpleTestCase):
    
    # For home
    def test_case_home_url(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)
    # For productpage
    def test_case_SearchView_url(self):
        url=reverse('productpage')
        self.assertEquals(resolve(url).func,SearchView)
    # For search
    def test_case_SearchView_url(self):
        url=reverse('SearchView')
        self.assertEquals(resolve(url).func,SearchView)

    def test_case_searchresult_url(self):
        url=reverse('searchresult')
        self.assertEquals(resolve(url).func,searchresult)

      # For edit
    def test_case_edit_url(self):
        url=reverse('edit')
        self.assertEquals(resolve(url).func,edit)