from selenium import webdriver

localhost : str = "http://localhost:8000"

browser : webdriver.Firefox = webdriver.Firefox()
browser.get(localhost)

assert "To-do" in browser.title, f"Browser title was {browser.title}"

browser.quit()