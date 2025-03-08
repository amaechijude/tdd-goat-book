import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


localhost: str = "http://localhost:8000"

class NewSiteVsitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser  = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_web_visit(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get(localhost)

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)


        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")  
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys("Buy peacock feathers")  

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(3)
        
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")  
       
        self.assertIn(
            "1: Buy peacock feathers", [row.text for row in rows]
            )

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peackock feather to make fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows]
        )
        self.assertIn(
            "2: Use peackock feather to make fly",
            [row.twxt for row in rows]
        )

        # Satisfied, she goes back to sleep

        self.fail("Finish the test")


if __name__ == "__main__":
    unittest.main()