from base.base_class import Base
from base.locators import *
import allure


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_locator_checkout_button(self):
        return self.get_locator(checkout_button_locator)

    # Actions
    def click_button(self):
        self.get_locator_checkout_button().click()
        print('Click button Checkout')

    # Methods
    def click_button_checkout(self):
        with allure.step("Next to client information"):
            self.get_current_url()
            self.click_button()
