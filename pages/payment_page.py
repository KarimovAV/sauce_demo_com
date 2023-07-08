from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from base.locators import *
import allure


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_button_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, finish_button_locator)))

    # Actions
    def click_button_finish(self):
        self.get_button_finish().click()
        print(f'Clicked button Finish')

    # Methods
    def next_to_finish(self):
        with allure.step("Next to Finish"):
            self.get_current_url()
            self.get_button_finish()
            self.click_button_finish()
