from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser,12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'),'100'))

    book = browser.find_element(By.ID,'book')
    book.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

   # robot = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
   # robot.click()

   # robot_rule = browser.find_element_by_xpath("//input[@id='robotsRule']")
   # robot_rule.click()

    button = browser.find_element(By.ID,'solve')
    button.click()
   


finally:
    time.sleep(20)
    browser.quit()
