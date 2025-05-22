from pages.login_page import LoginPage
from config import config

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url  # Verifica que entraste correctamente

