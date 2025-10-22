import allure

from data.recipe_data import RecipeData


class TestRecipesPage:

    @allure.title("Проверка создания рецепта")
    @allure.description("Проверка, что можно создать рецепт")
    def test_create_recipe_recipe_is_created(
        self,
        sign_in_page,
        sign_up_page,
        recipies_page,
        create_account_and_login,
        create_recipe_page,
        recipe_page,
    ):
        recipe_data = RecipeData.RECIPE_DATA
        recipies_page.click_on_create_recipe_tab()
        create_recipe_page.create_recipe(
            recipe_data["name"],
            recipe_data["ingredient"],
            recipe_data["amount"],
            recipe_data["cooking_time"],
            recipe_data["description"],
            recipe_data["file_name"],
        )
        recipe_page.wait_recipe_page_is_loaded()
        recipe_page.check_recipe_name_is_valid(recipe_data["name"])
