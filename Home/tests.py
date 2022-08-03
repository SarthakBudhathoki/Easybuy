from django.urls import resolve , reverse
from django.test import SimpleTestCase 
from Home.views import  *
# Create your tests here.
class TestUrls(SimpleTestCase):

      # For blog
    def test_case_blog_url(self):
        url=reverse('blog')
        self.assertEquals(resolve(url).func,showblog)

    # For creatorprofile week 6
    def test_case_creator_profile_url(self):
        url=reverse('creatorprofile')
        self.assertEquals(resolve(url).func,creatorprofile)

    #   # For categorie 
    def test_case_categorie_detail_url(self):
        url=reverse('categorie')
        self.assertEquals(resolve(url).func,categorie)
    
    # # For contact
    def test_case_contact_url(self):
        url=reverse('contact')
        self.assertEquals(resolve(url).func,contact)

    # # For store week 
    def test_case_store_url(self):
        url=reverse('store')
        self.assertEquals(resolve(url).func,store)

    # # For contact week 5
    def test_case_profile_url(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func,profile)

     # # For contact week 6
    def test_case_creator_url(self):
        url=reverse('creator')
        self.assertEquals(resolve(url).func,creator)

     # # For contact week 4
    def test_case_verify_payment_url(self):
        url=reverse('verify_payment')
        self.assertEquals(resolve(url).func,verify_payment)

     #for cart week 4
    def test_case_delete_cart_url(self):
        url=reverse('delete_cart',args=[1])
        self.assertEquals(resolve(url).func, delete_cart)

    def test_case_logoutcreator_url(self):
        url=reverse('logoutcreator')
        self.assertEquals(resolve(url).func, logoutcreator)
    
    #For Profile week 3
    def test_case_profile_url(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    # For search week 3
    def test_case_search_url(self):
        url=reverse('search')
        self.assertEquals(resolve(url).func, SearchView)    

    # For search week 6
    def test_case_logoutcreator_url(self):
        url=reverse('logoutcreator')
        self.assertEquals(resolve(url).func, logoutcreator)

    # For search week 7
    def test_case_admindashboard_url(self):
        url=reverse('admindashboard')
        self.assertEquals(resolve(url).func, admin_dashboard_view)

     # For search week 7
    def test_case_admindashboard_url(self):
        url=reverse('admindashboard')
        self.assertEquals(resolve(url).func, admin_dashboard_view)
