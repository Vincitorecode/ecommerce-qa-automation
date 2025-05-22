from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.finish_page import FinishPage
from config import config

def test_checkout(driver):
    login = LoginPage(driver)
    login.open(config.BASE_URL)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.product_is_in_cart()
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_info("John", "Doe", "12345")

    overview = OverviewPage(driver)
    overview.finish_checkout()

    finish = FinishPage(driver)
    assert finish.is_checkout_complete()
