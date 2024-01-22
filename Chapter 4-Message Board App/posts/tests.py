from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(text='its a simple test')

    def test_model(self):
        self.assertEqual(self.post.text, 'its a simple test')

class UrlsTest(TestCase):
    def test_url_exists_at_correct_location(self): # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self): 
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self): 
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
        
    def test_template_content(self): 
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")