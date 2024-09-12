import pytest
from core.ui.chrome_driver_manager_scd import ChromeDriverManager
from main.ui.pages.login_page import LoginPage
from conftest import is_user_logged_in
import config


def test_login(driver):
    # Instanciar la página de login
    login_page = LoginPage(driver)
    login_page.navigate_to(config.BASE_URL)

    # Realizar el login
    login_page.login(config.USERNAME, config.PASSWORD)

    # Verficiar si el login fue exitoso comprobando el titulo de la pagina
    titulo = driver.title
    print(f"Título de la página después del login: {titulo}")

    # Cambia el valor "Título esperado" por el título que debería tener la página tras iniciar sesión
    assert titulo == "Iniciar sesión", f"El título de la página no coincide. Título actual: {titulo}"
