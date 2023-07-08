import datetime


class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method Get Current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url: {get_url}')

    """Method Assert Word"""

    @staticmethod
    def assert_word(word, result):
        value_word = word.text
        assert value_word == result
        print(f'Check passed: (get value) {value_word} == (need value) {result}')

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot("C:\\Users\\Антон\\pythonProject\\sauce_demo_com\\screen\\" + name_screenshot)