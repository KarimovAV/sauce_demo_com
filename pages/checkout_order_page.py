from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from base.locators import *
import allure


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_checkout_success(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, checkout_text_success)))

    # Methods
    def checkout_order_page(self):
        with allure.step("Buy is success"):
            self.get_current_url()
            self.assert_word(self.get_checkout_success(), 'Thank you for your order!')
            self.get_screenshot()
