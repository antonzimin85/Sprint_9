from selenium.webdriver.common.by import By


class CreateRecipePageLocators:

    RECIPE_NAME_INPUT_FIELD = (
        By.XPATH,
        './/div[text()="Название рецепта"]/following-sibling::input',
    )
    INGREDIENT_INPUT_FIELD = (
        By.XPATH,
        './/div[text()="Ингредиенты"]/following-sibling::input',
    )
    INGREDIENT_LOCATOR = (By.XPATH, './/div[text()="{}"]')
    ADD_INGREDIENT_BUTTON = (By.XPATH, './/div[text()="Добавить ингредиент"]')
    INGREDIENT_AMOUNT_INPUT_FIELD = (
        By.XPATH,
        './/input[contains(@class, "ingredientsAmountValue")]',
    )
    COOKING_TIME_INPUT_FIELD = (
        By.XPATH,
        './/div[text()="Время приготовления"]/following-sibling::input',
    )
    RECIPE_DESCRIPTION_INPUT_FIELD = (
        By.XPATH,
        './/div[text()="Описание рецепта"]/following-sibling::textarea',
    )
    SELECT_FILE_BUTTON = (By.XPATH, './/input[contains(@class, "fileInput")]')
    CREATE_RECIPE_BUTTON = (By.XPATH, './/button[text()="Создать рецепт"]')
