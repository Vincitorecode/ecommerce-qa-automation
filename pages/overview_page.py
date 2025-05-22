from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OverviewPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    def finish_checkout(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
