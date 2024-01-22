from django.test import TestCase , SimpleTestCase
from django.urls import reverse
# Create your tests here.
class HomePageTest(SimpleTestCase):
    
    def test_url(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self): 
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Home page</h1>")

class AboutPageTest(SimpleTestCase):
    def test_url(self):
        res = self.client.get('/about/')
        self.assertEqual(res.status_code, 200)
        
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self): 
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>about file</h1>")