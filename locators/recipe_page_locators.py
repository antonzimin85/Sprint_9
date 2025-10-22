from selenium.webdriver.common.by import By


class RecipePageLocators:

    RECIPE_NAME = (By.XPATH, './/h1[contains(@class, "single-card__title")]')
    EDIT_RECIPE_BUTTON = (By.XPATH, './/a[text()="Редактировать рецепт"]')
