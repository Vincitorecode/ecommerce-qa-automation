from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
