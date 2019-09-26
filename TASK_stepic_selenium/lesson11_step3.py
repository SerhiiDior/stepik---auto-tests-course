from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('input.form-control.first:required')
    input1.send_keys('SASHA')
    input2 = browser.find_element_by_css_selector('input.form-control.second:required')
    input2.send_keys('Doctor')
    input3 = browser.find_element_by_css_selector('input.form-control.third:required')
    input3.send_keys('test@mail.ru')


    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    
    welcome_text = welcome_text_elt.text

    
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(8)
    browser.quit()

