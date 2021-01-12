from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
try:
    # Загрузка страницыy
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Поиск элементов
    x_element = browser.find_element_by_id ("input_value")
    x = x_element.text
    #num2 = browser.find_element_by_id ("num2")
    # Определяем функцию
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc (x)
    # Находим поле ввода и заполняем его
    answer = browser.find_element_by_id ("answer")
    answer.send_keys (y)
    # Ищем кнопку и скроллим
    button = browser.find_element_by_class_name ("btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # выбираем опции (ради и чекбоксы)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click() 
    # Выбор списка и элементов в нем
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value (z)
    # time.sleep (2)
    button.click()
    #submit_button = browser.find_element_by_css_selector(".btn")
    #submit_button.click()
finally:
    time.sleep(5)
    browser.quit()