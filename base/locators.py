# URL, URI
base_url = 'https://www.saucedemo.com/'
main_url_shops = 'https://www.saucedemo.com/inventory.html'
cart_shops = 'https://www.saucedemo.com/cart.html'
client_information = 'https://www.saucedemo.com/checkout-step-one.html'
payment_page = 'https://www.saucedemo.com/checkout-step-two.html'
checkout_complete = 'https://www.saucedemo.com/checkout-complete.html'

# Locators, Login page, base_url
user_name_locator = "//input[@id='user-name']"
password_locator = "//input[@id='password']"
login_button_locator = "//input[@id='login-button']"

incorrect_password = "//h3[@data-test='error']"

# Locators, Main shops, main_url_shops
check_value_products = "//span[@class='title']"

product_one_locator = "//button[@id='add-to-cart-sauce-labs-backpack']"
product_two_locator = "//button[@id='add-to-cart-sauce-labs-bike-light']"

cart_locator = "//a[@class='shopping_cart_link']"

# Locators, Cart, cart_shops
checkout_button_locator = "//button[@id='checkout']"

# Locators, Client information
first_name_locator = "//input[@id='first-name']"
last_name_locator = "//input[@id='last-name']"
zip_code_locator = "//input[@id='postal-code']"
continue_locator = "//input[@id='continue']"

# Locators, Payment page
finish_button_locator = "//button[@id='finish']"

# Locators, Checkout complete
checkout_text_success = "//h2[@class='complete-header']"
