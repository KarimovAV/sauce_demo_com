from base.base_class import Base
from base.locators import *
import allure


class PaymentPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_locator_button_finish(self):
        return self.get_locator(finish_button_locator)

    # Actions
    def click_button_finish(self):
        self.get_locator_button_finish().click()
        print(f'Clicked button Finish')

    # Methods
    def next_to_finish(self):
        with allure.step("Next to Finish"):
            self.get_current_url()
            self.click_button_finish()
