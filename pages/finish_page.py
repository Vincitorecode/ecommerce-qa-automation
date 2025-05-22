from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class FinishPage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def is_checkout_complete(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).is_displayed()
