from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.INVENTORY_CONTAINER)
            )
            return True
        except:
            return False

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MSG).text
        except:
            return None
        

