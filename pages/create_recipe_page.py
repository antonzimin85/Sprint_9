import allure

from config import ASSETS_DIR
from locators.create_recipe_page_locators import CreateRecipePageLocators
from pages.base_page import BasePage


class CreateRecipePage(BasePage):

    @allure.step("Вводим название рецепта")
    def enter_recipe_name(self, name):
        self.enter_text(CreateRecipePageLocators.RECIPE_NAME_INPUT_FIELD, name)

    @staticmethod
    def get_ingredient_locator_by_ingredient_name(ingredient_locator, ingredient_name):
        by, locator = ingredient_locator
        return by, locator.format(ingredient_name)

    @allure.step("Добавляем ингредиент")
    def add_ingredient(self, ingredient, ingredient_locator):
        ingredient_locator = self.get_ingredient_locator_by_ingredient_name(
            ingredient_locator, ingredient
        )
        self.enter_text(CreateRecipePageLocators.INGREDIENT_INPUT_FIELD, ingredient[:2])
        self.click_on_element(ingredient_locator)

    @allure.step("Вводим количество ингредиента")
    def enter_ingredient_amount(self, amount):
        self.enter_text(CreateRecipePageLocators.INGREDIENT_AMOUNT_INPUT_FIELD, amount)

    @allure.step('Кликаем на "Добавить ингредиент"')
    def click_on_add_ingredient_button(self):
        self.click_on_element(CreateRecipePageLocators.ADD_INGREDIENT_BUTTON)

    @allure.step("Вводим время приготовления")
    def enter_cooking_time(self, cooking_time):
        self.enter_text(CreateRecipePageLocators.COOKING_TIME_INPUT_FIELD, cooking_time)

    @allure.step("Вводим описание рецепта")
    def enter_recipe_description(self, description):
        self.enter_text(
            CreateRecipePageLocators.RECIPE_DESCRIPTION_INPUT_FIELD, description
        )

    @staticmethod
    def get_recipe_picture_path(file_name):
        return ASSETS_DIR / file_name

    @allure.step("Загружаем фото")
    def load_the_picture(self, file_name):
        file_path = self.get_recipe_picture_path(file_name)
        self.load_file(CreateRecipePageLocators.SELECT_FILE_BUTTON, str(file_path))

    @allure.step('Кликаем на кнопку "Создать рецепт"')
    def click_on_create_recipe_button(self):
        self.click_on_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)

    @allure.step("Создаем рецепт")
    def create_recipe(
        self, name, ingredient, amount, cooking_time, description, file_name
    ):
        self.enter_recipe_name(name)
        self.add_ingredient(ingredient, CreateRecipePageLocators.INGREDIENT_LOCATOR)
        self.enter_ingredient_amount(amount)
        self.click_on_add_ingredient_button()
        self.enter_cooking_time(cooking_time)
        self.enter_recipe_description(description)
        self.load_the_picture(file_name)
        self.click_on_create_recipe_button()
