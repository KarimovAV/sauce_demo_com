import time
from utilities.conftest import*
from pages.login_page import LoginPage

from base.input_data import *


def test_authorization_positive(set_up):
    print('Start test: test_authorization_positive')
    login = LoginPage(driver)
    login.authorization(user=correct_login_one, password=correct_password_one)
    time.sleep(10)
    print('End test: test_authorization_positive')


def test_authorization_incorrect_password(set_up):
    print('Start test: test_authorization_incorrect_password')
    login = LoginPage(driver)
    login.authorization_error(user=correct_login_one, password=incorrect_password_one)
    time.sleep(10)
    print('End test: test_authorization_incorrect_password')
