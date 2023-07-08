from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from base.locators import *
import allure


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, checkout_button_locator)))

    # Actions
    def click_button(self):
        self.get_checkout_button().click()
        print('Click button Checkout')

    # Methods
    def click_button_checkout(self):
        with allure.step("Next to client information"):
            self.get_current_url()
            self.get_checkout_button()
            self.click_button()
