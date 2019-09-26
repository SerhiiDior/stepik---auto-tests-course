from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math
import time


link = 'http://suninjuly.github.io/selects1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    z_element = browser.find_element(By.ID, 'num2')
    z = z_element.text
    y = int(x)+int(z)
    
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(y))
   # answer = browser.find_element(By.ID, 'answer')
   # answer.send_keys(y)

   # robot = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
   # robot.click()

   # robot_rule = browser.find_element_by_xpath("//input[@id='robotsRule']")
   # robot_rule.click()

    button = browser.find_element_by_css_selector('.btn-default')
    button.click()
   


finally:
    time.sleep(10)
    browser.quit()
