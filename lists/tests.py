from django.http import HttpRequest
from django.test import TestCase
from lists.views import home_page
# Create your tests here.

class BadMathsTests(TestCase):
    def test_maths(self):
        self.assertEqual(3*3, 9)

class HomePageTest(TestCase):
    def test_home_page_http_response(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")

        self.assertIn("<title>To-Do Lists</title>", html)
        self.assertTrue(html.startswith("<!DOCTYPE html>"))
        self.assertTrue(html.endswith("</html>"))

    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_form_post(self):
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertContains(response, "A new list item")
        self.assertTemplateUsed(response, "home.html")

