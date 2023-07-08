import pytest
import selenium.webdriver

driver = selenium.webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'


@pytest.fixture
def set_up():
    print('Start test')
    driver.get(base_url)
    driver.maximize_window()
    yield
    print('Test end')