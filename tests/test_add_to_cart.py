from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config import config


# tests/test_add_to_cart.py
def test_add_to_cart(driver):  # pytest inyecta el driver aquí automáticamente
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    login.login("standard_user", "secret_sauce")

    assert login.is_logged_in(), f"Login failed: {login.get_error_message()}"

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.product_is_in_cart(), "No product found in cart"



    