import allure

from locators.sign_up_page_locators import SignUpPageLocators
from pages.base_page import BasePage


class SignUpPage(BasePage):

    @allure.step("Вводим имя")
    def enter_first_name(self, first_name):
        self.enter_text(SignUpPageLocators.FIRST_NAME_INPUT_FIELD, first_name)

    allure.step("Вводим фамилию")

    def enter_last_name(self, last_name):
        self.enter_text(SignUpPageLocators.LAST_NAME_INPUT_FIELD, last_name)

    @allure.step("Вводим имя пользователя")
    def enter_user_name(self, user_name):
        self.enter_text(SignUpPageLocators.USER_NAME_INPUT_FIELD, user_name)

    @allure.step("Вводим email")
    def enter_email(self, email):
        self.enter_text(SignUpPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step("Вводим пароль")
    def enter_password(self, password):
        self.enter_text(SignUpPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Кликаем по кнопке "Создать аккаунт"')
    def click_on_create_account_button(self):
        self.click_on_element(SignUpPageLocators.CREATE_ACCOUNT_BUTTON)

    @allure.step('Заполняем все поля формы и кликаем по кнопке "Войти"')
    def create_account(self, first_name, last_name, user_name, email, password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_user_name(user_name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_create_account_button()
