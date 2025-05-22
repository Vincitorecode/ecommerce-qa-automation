from pages.login_page import LoginPage
from config import config
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(config.BASE_URL)
    login_page.login("standard_user", "secret_sauce")
    close_google_password_alert_if_present(driver)
    assert "inventory" in driver.current_url  # Verifica que entraste correctamente

def close_google_password_alert_if_present(driver):
    try:
        # Espera explícita para el botón "Aceptar" del alert de Google
        accept_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Aceptar') or contains(text(), 'Acaptar')]"))
        )
        print("Alert de Google encontrado")
        accept_button.click()
        print("Alert de Google cerrado")
    except TimeoutException:
        print("No se encontró el alert de Google")