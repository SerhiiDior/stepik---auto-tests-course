from selenium import webdriver
import os
import time

link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test_file.txt')

browser = webdriver.Chrome()

browser.get(link)

try:
    name=browser.find_element_by_name('firstname')
    name.send_keys('Serge')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Dior')

    email = browser.find_element_by_name('email')
    email.send_keys('test@mail.ru')

    download = browser.find_element_by_xpath("//input[@type='file']")
    download.send_keys(file_path)

    button = browser.find_element_by_css_selector('.btn-primary')
    button.click()
    
    

finally:
    time.sleep(15)
    browser.quit()
