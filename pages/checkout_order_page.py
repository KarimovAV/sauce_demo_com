from selenium.webdriver.common.by import By
from base.base_class import Base
from base.locators import *
import allure


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_locator_checkout_success(self):
        return self.get_locator(checkout_text_success)

    # Methods
    def checkout_order_page(self):
        with allure.step("Buy is success"):
            self.get_current_url()
            self.assert_word(self.get_locator_checkout_success(), 'Thank you for your order!')
            self.get_screenshot()
