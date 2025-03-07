from selenium import webdriver

localhost : str = "http://localhost:8000"

browser : webdriver.Firefox = webdriver.Firefox()
browser.get(localhost)

assert "Congratulations!" in browser.title
print("Ok")