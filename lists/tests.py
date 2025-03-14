from django.http import HttpRequest
from django.test import TestCase
from lists.views import home_page
from lists.models import Item
# Create your tests here.

# class BadMathsTests(TestCase):
#     def test_maths(self):
#         self.assertEqual(3*3, 9)

class HomePageTest(TestCase):

    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_form_post(self):
        response = self.client.post("/", data={"item_text": "A new list item"})

        self.assertContains(response, "A new list item")
        self.assertTemplateUsed(response, "home.html")

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) item")
        self.assertEqual(second_saved_item.text, "Item the second")
