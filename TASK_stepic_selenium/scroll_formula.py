from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://SunInJuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    robot = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    robot.click()

    robot_rule = browser.find_element_by_xpath("//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    robot_rule.click()

    button = browser.find_element_by_css_selector('.btn-primary')
    button.click()
   


finally:
    time.sleep(10)
    browser.quit()
