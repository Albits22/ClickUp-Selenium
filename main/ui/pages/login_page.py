from main.ui.locators.login_locators import *
from main.ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Definir los locators
    EMAIL_FIELD = (By.CSS_SELECTOR, "#login-email-input")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#login-password-input")
    LOGIN_BUTTON = (By.CSS_SELECTOR,
                    "span.login-page-new__main-form-button-text")

    def login(self, username, password):
        # Escribir el correo electrónico
        self.type_text(self.EMAIL_FIELD, username)
        # Escribir la contraseña
        self.type_text(self.PASSWORD_FIELD, password)
        # Hacer clic en el botón de login
        self.click(self.LOGIN_BUTTON)
