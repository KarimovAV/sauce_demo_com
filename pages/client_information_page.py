from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base
from base.locators import *
import allure

class ClientInformation(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, first_name_locator)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, last_name_locator)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, zip_code_locator)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, continue_locator)))

    # Actions
    def send_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print(f'Entered First Name: {first_name}')

    def send_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print(f'Entered Last Name: {last_name}')

    def send_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print(f'Entered zip code: {zip_code}')

    def click_continue(self):
        self.get_continue_button().click()
        print('Clicked button Continue')

    # Methods
    def fill_client_information(self, first_name, last_name, zip_code):
        with allure.step("Filled client information"):
            self.get_current_url()
            self.send_first_name(first_name=first_name)
            self.send_last_name(last_name=last_name)
            self.send_zip_code(zip_code=zip_code)
            self.click_continue()