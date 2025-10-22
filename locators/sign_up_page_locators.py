from selenium.webdriver.common.by import By


class SignUpPageLocators:

    FIRST_NAME_INPUT_FIELD = (By.XPATH, './/input[@name="first_name"]')
    LAST_NAME_INPUT_FIELD = (By.XPATH, './/input[@name="last_name"]')
    USER_NAME_INPUT_FIELD = (By.XPATH, './/input[@name="username"]')
    EMAIL_INPUT_FIELD = (By.XPATH, './/input[@name="email"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, './/input[@name="password"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Создать аккаунт"]')
