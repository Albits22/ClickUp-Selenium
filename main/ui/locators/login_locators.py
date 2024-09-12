from selenium.webdriver.common.by import By

# Locator para el campo de correo electrónico
EMAIL_FIELD = (By.CSS_SELECTOR, "#login-email-input")

# Locator para el campo de contraseña
PASSWORD_FIELD = (By.CSS_SELECTOR, "#login-password-input")

# Locator para el botón de "Iniciar sesión"
LOGIN_BUTTON = (By.CSS_SELECTOR, "span.login-page-new__main-form-button-text")
