from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_xpath('//button[@type="submit"]')
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)


    button = browser.find_element_by_css_selector('.btn-primary')
    button.click()
   


finally:
    time.sleep(10)
    browser.quit()
