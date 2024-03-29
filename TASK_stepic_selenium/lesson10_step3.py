from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_class_name('form-control.first')
    input1.send_keys('Serge')
    input2 = browser.find_element_by_class_name('form-control.second')
    input2.send_keys('Dior')
    input3 = browser.find_element_by_class_name('form-control.third')
    input3.send_keys('test@mail.ru')


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(8)
    browser.quit()
