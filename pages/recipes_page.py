import allure

from config import RECIPES_PAGE_URL
from locators.recipies_page_locators import RecipiesPageLocators
from pages.base_page import BasePage


class RecipiesPage(BasePage):

    @allure.step('Дожидаемся загрузки страницы "Рецепты"')
    def wait_recipies_page_is_loaded(self):
        self.wait_element_is_visible(RecipiesPageLocators.RECIPIES_PAGE_TITLE)

    @allure.step('Кликаем по табе "Создать рецепт"')
    def click_on_create_recipe_tab(self):
        self.click_on_element(RecipiesPageLocators.CREATE_RECIPE_TAB)

    @allure.step("Проверяем, что url соответствует странице recipies")
    def check_recipies_url(self):
        assert self.return_current_url() == RECIPES_PAGE_URL

    @allure.step('Проверяем, что отображается кнопка "Выход"')
    def check_logout_button_is_displayed(self):
        assert self.check_element_is_visible(RecipiesPageLocators.LOGOUT_BUTTON)
