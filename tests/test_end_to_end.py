import allure
from utilities.conftest import *
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.client_information_page import ClientInformation
from pages.payment_page import PaymentPage
from pages.checkout_order_page import CheckoutPage

from base.input_data import *


@allure.description("Test for end to end (authorization -> add products to cart -> next to buy")
def test_end_to_end(set_up):
    lp = LoginPage(driver)
    mp = MainPage(driver)
    cp = CartPage(driver)
    cip = ClientInformation(driver)
    pp = PaymentPage(driver)
    cop = CheckoutPage(driver)

    lp.authorization(user=correct_login_one, password=correct_password_one)
    mp.add_product_to_cart()
    cp.click_button_checkout()
    cip.fill_client_information(first_name=first_name_positive, last_name=last_name_positive, zip_code=zip_code_positive)
    pp.next_to_finish()
    cop.checkout_order_page()
    print('End test: test_end_to_end')

