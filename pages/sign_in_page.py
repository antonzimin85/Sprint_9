import allure

from config import BASE_URL, SIGN_IN_PAGE_URL
from locators.sign_in_page_locators import SignInPageLocators
from pages.base_page import BasePage


class SignInPage(BasePage):

    @allure.step("Открываем sign_in страницу ")
    def open_sign_in_page(self):
        self.open_url(BASE_URL)

    @allure.step("Дожидаемся загрузки sign_in страницы")
    def wait_sign_in_page_is_loaded(self):
        self.wait_element_is_visible(SignInPageLocators.ENTER_BUTTON)

    @allure.step("Вводим email")
    def enter_email(self, email):
        self.enter_text(SignInPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step("Вводим пароль")
    def enter_password(self, password):
        self.enter_text(SignInPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Кликаем по кнопке "Войти"')
    def click_on_enter_button(self):
        self.click_on_element(SignInPageLocators.ENTER_BUTTON)

    @allure.step('Кликаем по кнопке "Создать аккаунт"')
    def click_on_create_account_button(self):
        self.click_on_element(SignInPageLocators.CREATE_ACCOUNT_BUTTON)

    @allure.step("Проверяем, что url соответствует sign_in странице")
    def check_sign_in_page_url(self):
        assert self.return_current_url() == SIGN_IN_PAGE_URL

    @allure.step("Проверяем, что форма авторизации отображается")
    def check_authorization_form_is_displayed(self):
        assert self.check_element_is_visible(SignInPageLocators.EMAIL_INPUT_FIELD)
