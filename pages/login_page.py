from base.base_class import Base
from base.locators import *
import allure


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_locator_user_name(self):
        return self.get_locator(user_name_locator)

    def get_locator_password(self):
        return self.get_locator(password_locator)

    def get_locator_login_button(self):
        return self.get_locator(login_button_locator)

    def get_locator_word(self):
        return self.get_locator(check_value_products)

    def get_locator_text_error(self):
        return self.get_locator(incorrect_password)

    # Actions
    def input_user_name(self, user_name):
        self.get_locator_user_name().send_keys(user_name)
        print(f'Input login: {user_name}')

    def input_password(self, user_password):
        self.get_locator_password().send_keys(user_password)
        print(f'Input password: {user_password}')

    def click_login_button(self):
        self.get_locator_login_button().click()
        print('Clicked login button')

    # Methods
    def authorization(self, user, password):
        with allure.step("Authorization"):
            self.get_current_url()
            self.input_user_name(user_name=user)
            self.input_password(user_password=password)
            self.click_login_button()
            self.assert_word(self.get_locator_word(), 'Products')

    def authorization_error(self, user, password):
        self.get_current_url()
        self.input_user_name(user_name=user)
        self.input_password(user_password=password)
        self.click_login_button()
        self.assert_word(self.get_locator_text_error(), 'Epic sadface: Username and password do not match any user in this service')

