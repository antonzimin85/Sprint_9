from selenium.webdriver.common.by import By


class SignInPageLocators:

    SIGN_IN_PAGE_TITLE = (By.XPATH, './/h1[text()="Войти на сайт"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, './/a[text()="Создать аккаунт"]')
    ENTER_BUTTON_HEADER = (By.XPATH, './/a[text()="Войти"]')
    EMAIL_INPUT_FIELD = (By.XPATH, './/input[@name="email"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, './/input[@name="password"]')
    ENTER_BUTTON = (By.XPATH, './/button[text()="Войти"]')
