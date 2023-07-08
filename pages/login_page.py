from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from base.locators import *
import allure


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, user_name_locator)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, password_locator)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, login_button_locator)))

    def get_word_for_check(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, check_value_products)))

    def get_text_error(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, incorrect_password)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print(f'Input login: {user_name}')

    def input_password(self, user_password):
        self.get_password().send_keys(user_password)
        print(f'Input password: {user_password}')

    def click_login_button(self):
        self.get_login_button().click()
        print('Clicked login button')

    # Methods
    def authorization(self, user, password):
        with allure.step("Authorization"):
            self.get_current_url()
            self.input_user_name(user_name=user)
            self.input_password(user_password=password)
            self.click_login_button()
            self.assert_word(self.get_word_for_check(), 'Products')

    def authorization_error(self, user, password):
        self.get_current_url()
        self.input_user_name(user_name=user)
        self.input_password(user_password=password)
        self.click_login_button()
        self.assert_word(self.get_text_error(), 'Epic sadface: Username and password do not match any user in this service')

