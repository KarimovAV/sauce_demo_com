import pytest
import selenium.webdriver

options = selenium.webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = selenium.webdriver.Chrome(options=options)
base_url = 'https://www.saucedemo.com/'


@pytest.fixture
def set_up():
    print('Start test')
    driver.get(base_url)
    driver.maximize_window()
    yield
    print('Test end')