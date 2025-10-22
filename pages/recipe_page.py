import allure

from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage


class RecipePage(BasePage):

    @allure.step("Дожидаемся загрузки страницы созданного рецепта")
    def wait_recipe_page_is_loaded(self):
        self.wait_element_is_visible(RecipePageLocators.RECIPE_NAME)

    @allure.step("Проверка, что название рецепта соответствует введенному при создании")
    def check_recipe_name_is_valid(self, recipe_name):
        assert self.return_element_text(RecipePageLocators.RECIPE_NAME) == recipe_name
