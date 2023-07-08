import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
from base.locators import *


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters
    def get_product_one(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, product_one_locator)))

    def get_product_two(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, product_two_locator)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, cart_locator)))

    # Actions
    def click_product_one(self):
        self.get_product_one().click()
        print('Click product 1')

    def click_product_two(self):
        self.get_product_two().click()
        print('Click product 2')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')

    # Methods
    def add_product_to_cart(self):
        with allure.step("Add products to cart"):
            self.get_current_url()
            self.click_product_one()
            self.click_product_two()
            self.click_cart()
