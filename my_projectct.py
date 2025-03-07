from selenium import webdriver

localhost = "https://tailorconnect.store"
browser = webdriver.Firefox()

browser.get(localhost)
assert "TailorConnect" in browser.title

print("Ok")