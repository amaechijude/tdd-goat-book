from selenium import webdriver
import unittest
localhost: str = "http://localhost:8000"

class NewSiteVsitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser  = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_new_visitors(self):
        self.browser.get(localhost)

        self.assertIn("To-do", self.browser.title)

        self.fail("Finish the test")


if __name__ == "__main__":
    unittest.main()