from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")  # el primer botón "Add to cart"
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        # Esperar que el botón esté visible y hacer click en el primero
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
