import allure


class TestSignInPage:

    @allure.title("Проверка Авторизации")
    @allure.description("Проверяем, что можно авторизоваться")
    def test_sign_in_page_is_opened(
        self, sign_in_page, create_account, recipies_page, new_user_data
    ):
        sign_in_page.wait_sign_in_page_is_loaded()
        sign_in_page.enter_email(new_user_data["user_name"])
        sign_in_page.enter_password(new_user_data["password"])
        sign_in_page.click_on_enter_button()
        recipies_page.wait_recipies_page_is_loaded()
        recipies_page.check_recipies_url()
        recipies_page.check_logout_button_is_displayed()
