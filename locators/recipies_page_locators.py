from selenium.webdriver.common.by import By


class RecipiesPageLocators:

    RECIPIES_PAGE_TITLE = (By.XPATH, './/h1[text()="Рецепты"]')
    LOGOUT_BUTTON = (By.XPATH, './/a[text()="Выход"]')
    CREATE_RECIPE_TAB = (By.XPATH, './/a[text()="Создать рецепт"]')
