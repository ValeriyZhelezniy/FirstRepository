import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time

@pytest.mark.ui
def test_check_incorrect_username():
    #Створення обєкту для керування браузером
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #Знаходимо поле, в яке будемо ввоити неправильне імя користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    #Вводимо неправильне імя користувача або поштову адресу
    login_elem.send_keys("valeriy@ukr.net")
    time.sleep(3)

    #знаходимо поле, в яке будемо вводити неправилний пароль
    pass_elem = driver.find_element(By.ID, "password")

    #вводимо неправильний пароль
    pass_elem.send_keys("wrong passwords")
    
    # Знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, 'commit')

    #емулюємо клік лівою клавішою миші
    btn_elem.click()

    #перевіряємо що назва сторінки така як очікуємо
    assert driver.title == "Sign in to Github - Github"
    time.sleep(5)   

    #закриваємо браузер
    driver.close()
