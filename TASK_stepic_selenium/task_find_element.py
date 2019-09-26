from selenium import webdriver


browser = webdriver.Chrome()
browser.implicitly_wait(0.5)

browser.get('http://suninjuly.github.io/cats.html')

button = browser.find_element_by_id("button")
