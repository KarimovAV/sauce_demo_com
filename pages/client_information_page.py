from base.base_class import Base
from base.locators import *
import allure

class ClientInformation(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_locator_first_name(self):
        return self.get_locator(first_name_locator)

    def get_locator_last_name(self):
        return self.get_locator(last_name_locator)

    def get_locator_zip_code(self):
        return self.get_locator(zip_code_locator)

    def get_locator_continue_button(self):
        return self.get_locator(continue_locator)

    # Actions
    def send_first_name(self, first_name):
        self.get_locator_first_name().send_keys(first_name)
        print(f'Entered First Name: {first_name}')

    def send_last_name(self, last_name):
        self.get_locator_last_name().send_keys(last_name)
        print(f'Entered Last Name: {last_name}')

    def send_zip_code(self, zip_code):
        self.get_locator_zip_code().send_keys(zip_code)
        print(f'Entered zip code: {zip_code}')

    def click_continue(self):
        self.get_locator_continue_button().click()
        print('Clicked button Continue')

    # Methods
    def fill_client_information(self, first_name, last_name, zip_code):
        with allure.step("Filled client information"):
            self.get_current_url()
            self.send_first_name(first_name=first_name)
            self.send_last_name(last_name=last_name)
            self.send_zip_code(zip_code=zip_code)
            self.click_continue()