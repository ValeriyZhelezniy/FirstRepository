from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        #знаходимо поле в яке будемо вводити неправильне імя користувача або поштову адресу
        login_elem = self.driver.find_element(By.ID, 'login field')

        #вводимо неправльно імя користувачва або поштову адресу
        login_elem.send_keys(username)

        #знаходимо поле в яке будмо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, 'password')

        #вводимо неправильно пароль
        pass_elem.send_keys(password)

        #знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.NAME, 'commit')

        #емолюємо клік лівою кнопкою миші
        btn_elem.click()

    def check_title(self, espected_title):
        return self.driver.title == expected title            