from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import *

# Create your tests here.

class BlogTests(TestCase):

    def setupTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email = "test@email.com", password= "secret"
        )

        cls.post = Post.object.create(
            title = "A good title",
            body = "Nice body content",
            author=cls.user,
        )

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good tiile")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.body}", "nice body content")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(responce, "nice body content")
        self.asserTemplateused(responce,"home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(on_response.status_code,400)
        self.assertContains(response,"A good title")
        self.asserTemplateused(response,"post_detail.html")
        
    



