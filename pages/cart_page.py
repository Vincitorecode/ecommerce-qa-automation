# pages/cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CART_ITEM = (By.CSS_SELECTOR, ".cart_item")

    def __init__(self, driver):
        self.driver = driver

    def product_is_in_cart(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.CART_ITEM)
            )
            return True
        except:
            return False

